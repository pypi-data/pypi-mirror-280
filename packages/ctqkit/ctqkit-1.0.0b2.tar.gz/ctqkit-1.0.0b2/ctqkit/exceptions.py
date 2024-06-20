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

"""Exceptions for errors raised by Ctqkit."""


class CtqKitError(Exception):
    """Base class for errors raised by CtqKit."""

    def __init__(self, message):
        """Set the error message."""
        super().__init__(message)
        self.message = message

    def __str__(self):
        """Return the message."""
        return repr(self.message)


class VisualizationError(CtqKitError):
    """
    A custom exception class for representing errors in visualization processes.

    """

    def __init__(self, message):
        """
        Initializes a VisualizationError exception instance.

        Args:
            message: str - The error message describing the issue in detail.
        """
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        """
        Returns a string representation of the exception.

        Returns:
            str - The error message as a string.
        """
        return self.message


class CtqKitRequestError(CtqKitError):
    """Class for request errors raised by CtqKit."""

    def __init__(self, message, status_code=None):
        """Initialize the exception with a message and optional status code."""
        super().__init__(message)
        self.status_code = status_code
        if status_code is not None:
            self.message = f"Request failed with status code {status_code}: {message}"
        else:
            self.message = message


class CtqKitInputParaError(CtqKitError):
    """Class for input errors raised by CtqKit."""
