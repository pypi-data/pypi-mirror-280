''' An interface to DART
'''
from . import utils
import subprocess
import os
import f90nml
import x4c
import numpy as np
import ipywidgets as wgts
from IPython.display import display

import matplotlib.pyplot as plt

class DART:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        utils.p_header(f'>>> DART.root_dir: {self.root_dir}')


    def compile_model(self, model_name, build_mode='nompi'):
        work_dir = os.path.join(self.root_dir, f'models/{model_name}/work')
        cmd = f'cd {work_dir} && ./quickbuild.sh {build_mode}'
        utils.run_shell(cmd)

    def init_model(self, model_name):
        work_dir = os.path.join(self.root_dir, f'models/{model_name}/work')
        supported_models = {
            'lorenz_63': Lorenz63,
            'lorenz_96': Lorenz96,
            'forced_lorenz_96': ForcedLorenz96,
        }

        if model_name in supported_models:
            return supported_models[model_name](work_dir)
        else:
            return Model(work_dir)

class Model:
    def __init__(self, work_dir, nml_path=None):
        self.work_dir = work_dir
        utils.p_header(f'>>> Model.work_dir: {self.work_dir}')

        if nml_path is None:
            self.nml_path = os.path.join(self.work_dir, 'input.nml')
        else:
            self.nml_path = nml_path
        utils.p_header(f'>>> Model.nml_path: {self.nml_path}')

        self.params = f90nml.read(self.nml_path)
        utils.p_success(f'>>> Model.params created')

    def update_params(self, group, **kws):
        self.params[group].update(kws)
        self.params.write(self.nml_path, force=True)

    def rm_params(self, group, param_list):
        if type(param_list) not in (tuple, list):
            param_list = [param_list]

        for p in param_list:
            try:
                del(self.params[group][p])
            except:
                pass

        self.params.write(self.nml_path, force=True)

    def run(self, program, verbose=False, **kws):
        group = f'{program}_nml'
        if len(kws) > 0:
            self.update_params(group, **kws)

        if verbose:
            utils.p_header(f'>>> Run `{program}` with parameters:')
            utils.print_nml(self.nml_path, group)
        cmd = f'cd {self.work_dir} && ./{program}'
        utils.run_shell(cmd)

    @property
    def input(self):
        fpath = self.params['perfect_model_obs_nml']['input_state_files']
        ds = x4c.open_dataset(os.path.join(self.work_dir, fpath))
        return ds

    @property
    def output(self):
        fpath = self.params['perfect_model_obs_nml']['output_state_files']
        ds = x4c.open_dataset(os.path.join(self.work_dir, fpath))
        return ds

    @property
    def preassim(self):
        ds = x4c.open_dataset(os.path.join(self.work_dir, 'preassim.nc'))
        return ds

    @property
    def analysis(self):
        ds = x4c.open_dataset(os.path.join(self.work_dir, 'analysis.nc'))
        return ds

    @property
    def filter_input(self):
        ds = x4c.open_dataset(os.path.join(self.work_dir, 'filter_input.nc'))
        return ds

    @property
    def filter_output(self):
        ds = x4c.open_dataset(os.path.join(self.work_dir, 'filter_output.nc'))
        return ds

    @property
    def perfect_input(self):
        ds = x4c.open_dataset(os.path.join(self.work_dir, 'perfect_input.nc'))
        return ds

    @property
    def perfect_output(self):
        ds = x4c.open_dataset(os.path.join(self.work_dir, 'perfect_output.nc'))
        return ds

    @property
    def true_state(self):
        ds = x4c.open_dataset(os.path.join(self.work_dir, 'true_state.nc'))
        return ds

    def get_ncdata(self, fname):
        ds = x4c.open_dataset(os.path.join(self.work_dir, fname))
        return ds

class Lorenz63(Model):
    def __init__(self, work_dir):
        super().__init__(work_dir)

    def plot_it(self, it):
        x4c.set_style('journal', font_scale=1.2)
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(projection='3d')

        state_dict = {
            'true_state': self.true_state.state.mean('member'),
            'preassim': self.preassim.state_mean,
            'analysis': self.analysis.state_mean,
        }

        clr_dict = {
            'true_state': 'k',
            'preassim': 'tab:cyan',
            'analysis': 'tab:orange',
        }

        for k, sm in state_dict.items():
            ax.plot(sm[:it+1,0], sm[:it+1,1], sm[:it+1,2], color=clr_dict[k])
            ax.scatter(sm[it,0], sm[it,1], sm[it,2], color=clr_dict[k], s=100, label=k)

        ax.set_title('Lorenz 63', fontweight='bold')
        ax.set_title(f'Step: {it:04d}', loc='right')
        ax.set_xlabel('x', fontweight='bold')
        ax.set_ylabel('y', fontweight='bold')
        ax.set_zlabel('z', fontweight='bold')
        ax.set_xlim(-30, 30)
        ax.set_ylim(-30, 30)
        ax.set_zlim(0, 50)
        ax.legend(frameon=False)
        ax.set_box_aspect(aspect=None, zoom=0.8)
        plt.show(fig)

    def plot(self, it=None, min=0, max=None, step=1, style='play'):
        if it is not None:
            return self.plot_it(it)
        else:
            if max is None:
                max = len(self.preassim.time)-1

            if style == 'slider':
                slider = wgts.IntSlider(min=min, max=max, step=step, description='Step')
                wgts.interact(self.plot_it, it=slider)
            elif style == 'play':
                play = wgts.Play(min=min, max=max, step=step)
                wgts.interact(self.plot_it, it=play)


class Lorenz96(Model):
    def __init__(self, work_dir):
        super().__init__(work_dir)

    def plot_it(self, it):
        x4c.set_style('web', font_scale=1.2)
        fig = plt.figure(figsize=(6, 6))
        ax = fig.add_subplot(polar=True)

        state_dict = {
            'true_state': self.true_state.state.mean('member'),
            'preassim': self.preassim.state_mean,
            'analysis': self.analysis.state_mean,
        }

        clr_dict = {
            'true_state': 'k',
            'preassim': 'tab:cyan',
            'analysis': 'tab:orange',
        }

        for k, v in state_dict.items():
            sm = v[it]
            N = len(sm['location'])
            sm = list(sm.values)
            sm.append(sm[0])
            theta = list(np.linspace(0, 2 * np.pi, N, endpoint=False))
            theta.append(theta[0])
            ax.plot(theta, sm, color=clr_dict[k], label=k)
            ax.scatter(theta, sm, marker='o', color=clr_dict[k])

        ax.set_title('Lorenz 96', fontweight='bold')
        ax.set_title(f'Step: {it:04d}', loc='right')
        ax.legend(frameon=False, bbox_to_anchor=(1.5, 1), loc='upper right')
        ax.set_rlim(-20, 20)
        plt.show(fig)

    def plot(self, it=None, min=0, max=None, step=1, style='play'):
        if it is not None:
            return self.plot_it(it)
        else:
            if max is None:
                max = len(self.preassim.time)-1

            if style == 'slider':
                slider = wgts.IntSlider(min=min, max=max, step=step, description='Step')
                wgts.interact(self.plot_it, it=slider)
            elif style == 'play':
                play = wgts.Play(min=min, max=max, step=step)
                wgts.interact(self.plot_it, it=play)


class ForcedLorenz96(Model):
    def __init__(self, work_dir):
        super().__init__(work_dir)

    def plot_it(self, it):
        x4c.set_style('web', font_scale=1.2)
        fig = plt.figure(figsize=(6, 6))
        ax = fig.add_subplot(polar=True)

        state_dict = {
            'true_state': self.true_state.state.mean('member'),
            'preassim': self.preassim.state_mean,
            'analysis': self.analysis.state_mean,
        }
        clr_dict = {
            'true_state': 'k',
            'preassim': 'tab:cyan',
            'analysis': 'tab:orange',
        }

        for k, v in state_dict.items():
            sm = v[it]
            N = len(sm['location'])
            sm = list(sm.values)
            sm.append(sm[0])
            theta = list(np.linspace(0, 2 * np.pi, N, endpoint=False))
            theta.append(theta[0])
            ax.plot(theta, sm, color=clr_dict[k], label=k)
            ax.scatter(theta, sm, marker='o', color=clr_dict[k])

        ax.set_title('Forced Lorenz 96', fontweight='bold')
        ax.set_title(f'Step: {it:04d}', loc='right')
        ax.legend(frameon=False, bbox_to_anchor=(1.5, 1), loc='upper right')
        ax.set_rlim(-20, 20)
        plt.show(fig)

    def plot(self, it=None, min=0, max=None, step=1, style='play'):
        if it is not None:
            return self.plot_it(it)
        else:
            if max is None:
                max = len(self.preassim.time)-1

            if style == 'slider':
                slider = wgts.IntSlider(min=min, max=max, step=step, description='Step')
                wgts.interact(self.plot_it, it=slider)
            elif style == 'play':
                play = wgts.Play(min=min, max=max, step=step)
                wgts.interact(self.plot_it, it=play)