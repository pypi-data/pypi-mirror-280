# ViCodePy - A video coder for psychological experiments
#
# Copyright (C) 2024 Esteban Milleret
# Copyright (C) 2024 Rafael Laboissière
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.

# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
# Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program. If not, see <https://www.gnu.org/licenses/>.


def milliseconds_to_formatted_string(milliseconds):
    """
    Converts milliseconds to a string in the format hh:mm:ss.ssss.
    """

    # Convert milliseconds to seconds
    total_seconds = milliseconds / 1000

    # Extract hours, minutes, seconds
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Format time string with leading zeros
    time_string = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"

    # Extract milliseconds (avoiding floating-point rounding issues)
    milliseconds = milliseconds % 1000
    millisecond_string = f"{milliseconds:03d}"  # Pad with leading zeros

    return f"{time_string}.{millisecond_string}"


def milliseconds_to_seconds(milliseconds) -> float:
    """Converts milliseconds to seconds"""
    return milliseconds / 1000


def seconds_to_milliseconds(seconds) -> float:
    """Converts milliseconds to seconds"""
    return seconds * 1000
