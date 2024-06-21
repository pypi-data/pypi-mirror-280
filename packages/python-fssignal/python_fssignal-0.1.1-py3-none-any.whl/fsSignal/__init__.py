__version__ = "0.1.1"
__doc__ = """
Signal capturer v{}
Copyright (C) 2021 Fusion Solutions KFT <contact@fusionsolutions.io>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/lgpl.txt>.
""".format(__version__)
from .abcs import T_Locker, T_Signal
from .fsSignal import KillSignal, SignalIterator, Signal, SoftSignal, HardSignal, BaseSignal, SignalLocker, ExtendedLocker
__all__ = ("KillSignal", "SignalIterator", "Signal", "SoftSignal", "HardSignal", "BaseSignal", "SignalLocker", "ExtendedLocker",
"T_Locker", "T_Signal")
