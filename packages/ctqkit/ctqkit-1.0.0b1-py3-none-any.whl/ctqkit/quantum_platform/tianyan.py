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

"""
TianYan quantum platform
"""
from typing import Union, List

from .base import BasePlatform, QuantumLanguage
from ..exceptions import CtqKitError
from ..utils.laboratory_utils import LaboratoryUtils


class TianYanPlatform(BasePlatform):
    """
    Tian yan quantum computing cloud quantum_platform
    """
    SCHEME = 'https'
    DOMAIN = 'qc.zdxlz.com'
    LOGIN_PATH = '/qccp-auth/oauth2/opnId'
    CREATE_LAB_PATH = '/qccp-quantum/sdk/experiment/save'
    SAVE_EXP_PATH = '/qccp-quantum/sdk/experiment/detail/save'
    RUN_EXP_PATH = '/qccp-quantum/sdk/experiment/detail/run'
    SUBMIT_EXP_PATH = '/qccp-quantum/sdk/experiment/submit'
    # create exp and run path
    CREATE_EXP_AND_RUN_PATH = '/qccp-quantum/sdk/experiment/temporary/save'
    QUERY_EXP_PATH = '/qccp-quantum/sdk/experiment/result/find'
    # download config path
    DOWNLOAD_CONFIG_PATH = '/qccp-quantum/sdk/experiment/download/config'
    # qics check regular path
    QCIS_CHECK_REGULAR_PATH = '/qccp-quantum/sdk/experiment/qcis/rule/verify'
    # get exp circuit path
    GET_EXP_CIRCUIT_PATH = '/qccp-quantum/sdk/experiment/getQcis/by/taskIds'
    # machine list path
    MACHINE_LIST_PATH = '/qccp-quantum/sdk/quantumComputer/list'
    # re execute path
    RE_EXECUTE_TASK_PATH = '/qccp-quantum/sdk/experiment/resubmit'
    # stop running exp path
    STOP_RUNNING_EXP_PATH = ''

    def run_experiment(
            self,
            exp_id: str,
            num_shots: int = 10000,
            is_verify: bool = True
    ):
        """
        running the experiment returns the query result id.

        Args:
            exp_id: experimental id. the id returned by the save_experiment interface.
            num_shots: number of repetitions per experiment. Defaults to 12000.
            is_verify: Is the circuit verified.

        Returns:
            experiment task query id.
        """
        data = {
            "exp_id": exp_id,
            "shots": num_shots,
            "is_verify": is_verify,
        }
        result = self._send_request(path=self.RUN_EXP_PATH, data=data, method='post')
        return result.get('data').get('query_id')

    # pylint: disable=too-many-arguments
    def submit_experiment(
            self,
            circuit: Union[str, List[str]],
            language: QuantumLanguage,
            name: str = None,
            parameters: List[List[str]] = None,
            values: List[List[float]] = None,
            lab_id: str = None,
            lab_name: str = None,
            num_shots: int = 12000,
            machine_name: str = None,
            is_verify: bool = True
    ):
        """
        running the experiment returns the query result id.

        Args:
            circuit:
            language:
            name:
            parameters:
            values:
            lab_id:
            lab_name:
            num_shots: number of repetitions per experiment. Defaults to 12000.
            machine_name:
            is_verify: Is the circuit verified.

        Returns:
            experiment task query id.
        """
        if isinstance(circuit, str):
            circuit = [circuit]
        if parameters or values:
            assert len(parameters) == len(circuit) == len(values), \
                CtqKitError("The length of parameters, circuits, and values must be equal")
            lab_util = LaboratoryUtils()
            circuit = lab_util.assign_parameters(circuit, parameters, values)
            if not circuit:
                raise CtqKitError("Unable to assign a value to circuit, please check circuit.")

        data = {
            "circuit": circuit,
            "language": language.value,
            "name": name,
            "lab_id": lab_id,
            "lab_name": lab_name,
            "shots": num_shots,
            "computerCode": machine_name or self.machine_name,
            "is_verify": is_verify,
        }
        result = self._send_request(path=self.SUBMIT_EXP_PATH, data=data, method='post')
        return result.get('data').get('query_ids')
