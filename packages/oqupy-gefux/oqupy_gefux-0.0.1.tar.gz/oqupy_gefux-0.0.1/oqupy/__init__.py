"""
A Python 3 package to efficiently compute non-Markovian open quantum systems.

This open source project aims to facilitate versatile numerical tools to
efficiently compute the dynamics of quantum systems that are possibly strongly
coupled to a structured environment. It allows to conveniently apply the so
called time evolving matrix product operator method (TEMPO) [1], as well as
the process tensor TEMPO method (PT-TEMPO) [2].

[1] A. Strathearn, P. Kirton, D. Kilda, J. Keeling and
    B. W. Lovett,  *Efficient non-Markovian quantum dynamics using
    time-evolving matrix product operators*, Nat. Commun. 9, 3322 (2018).
[2] G. E. Fux, E. Butler, P. R. Eastham, B. W. Lovett, and
    J. Keeling, *Efficient exploration of Hamiltonian parameter space for
    optimal control of non-Markovian open quantum systems*, arXiv2101.?????
    (2021).
"""
from oqupy.version import __version__

# all API functionallity is in __all__
__all__ = [
    'AugmentedMPS',
    'Bath',
    'ChainControl',
    'CustomCorrelations',
    'CustomSD',
    'compute_correlations',
    'compute_correlations_nt',
    'compute_dynamics',
    'compute_dynamics_with_field',
    'compute_gradient_and_dynamics',
    'Control',
    'Dynamics',
    'FileProcessTensor',
    'GibbsParameters',
    'GibbsTempo',
    'gibbs_tempo_compute',
    'guess_tempo_parameters',
    'helpers',
    'import_process_tensor',
    'MeanFieldDynamics',
    'MeanFieldSystem',
    'MeanFieldTempo',
    'operators',
    'ParameterizedSystem',
    'PowerLawSD',
    'PtTebd',
    'PtTebdParameters',
    'PtTempo',
    'pt_tempo_compute',
    'SimpleProcessTensor',
    'state_gradient',
    'System',
    'SystemChain',
    'Tempo',
    'tempo_compute',
    'TempoParameters',
    'TimeDependentSystem',
    'TimeDependentSystemWithField',
    'TrivialProcessTensor',
    'TwoTimeBathCorrelations',
    ]

# -- Modules in alphabetical order --------------------------------------------

from oqupy.bath import Bath

from oqupy.bath_dynamics import TwoTimeBathCorrelations

from oqupy.system_dynamics import compute_correlations
from oqupy.system_dynamics import compute_correlations_nt
from oqupy.system_dynamics import compute_dynamics
from oqupy.system_dynamics import compute_dynamics_with_field

from oqupy.control import Control
from oqupy.control import ChainControl

from oqupy.bath_correlations import CustomCorrelations
from oqupy.bath_correlations import CustomSD
from oqupy.bath_correlations import PowerLawSD

from oqupy.dynamics import Dynamics
from oqupy.dynamics import MeanFieldDynamics

from oqupy.gradient import state_gradient
from oqupy.gradient import compute_gradient_and_dynamics

from oqupy import helpers

from oqupy.mps_mpo import AugmentedMPS

from oqupy import operators

from oqupy.process_tensor import import_process_tensor
from oqupy.process_tensor import TrivialProcessTensor
from oqupy.process_tensor import SimpleProcessTensor
from oqupy.process_tensor import FileProcessTensor

from oqupy.pt_tebd import PtTebd
from oqupy.pt_tebd import PtTebdParameters

from oqupy.system import System
from oqupy.system import SystemChain
from oqupy.system import TimeDependentSystem
from oqupy.system import TimeDependentSystemWithField
from oqupy.system import MeanFieldSystem
from oqupy.system import ParameterizedSystem

from oqupy.pt_tempo import PtTempo
from oqupy.pt_tempo import pt_tempo_compute

from oqupy.tempo import Tempo
from oqupy.tempo import TempoParameters
from oqupy.tempo import GibbsTempo
from oqupy.tempo import GibbsParameters
from oqupy.tempo import MeanFieldTempo
from oqupy.tempo import guess_tempo_parameters
from oqupy.tempo import tempo_compute
from oqupy.tempo import gibbs_tempo_compute
