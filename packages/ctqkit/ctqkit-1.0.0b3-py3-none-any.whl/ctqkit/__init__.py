# This code is part of ctqkit.
#
# (C) Copyright China Telecom Quantum Group, QuantumCTek Co., Ltd.,
# Center for Excellence in Quantum Information and Quantum Physics 2024.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""ctqkit"""

from .utils.qcis_to_qasm import QcisToQasm
from .utils.qasm_to_qcis.qasm_to_qcis import QasmToQcis
from .quantum_platform import BasePlatform, TianYanPlatform, GuoDunPlatform
