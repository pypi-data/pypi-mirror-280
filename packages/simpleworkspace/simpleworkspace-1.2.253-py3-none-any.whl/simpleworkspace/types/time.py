from enum import Enum as _Enum
from decimal import Decimal

class TimeEnum(_Enum):
    '''relative to seconds'''
    NanoSecond  = 0.000000001
    MicroSecond = 0.000001 
    MilliSecond = 0.001
    Second = 1
    Minute = 60
    Hour = Minute * 60
    Day = 24 * Hour
    Week = 7 * Day


class TimeSpan:
    def __init__(self, nanoSeconds:float=0, microSeconds:float=0, milliSeconds:float=0, seconds:float=0, minutes:float=0, hours:float=0, days:float=0, weeks:float=0):
        self._seconds = 0
        if(nanoSeconds > 0):
            self._seconds += nanoSeconds * TimeEnum.NanoSecond.value
        if(microSeconds):
            self._seconds += microSeconds * TimeEnum.MicroSecond.value
        if(milliSeconds > 0):
            self._seconds += milliSeconds * TimeEnum.MilliSecond.value
        if(seconds > 0):
            self._seconds += seconds
        if(minutes > 0):
            self._seconds += minutes * TimeEnum.Minute.value
        if(hours > 0):
            self._seconds += hours * TimeEnum.Hour.value
        if(days > 0):
            self._seconds += days * TimeEnum.Day.value
        if(weeks > 0):
            self._seconds += weeks * TimeEnum.Week.value
        return
    
    @property
    def TotalNanoSeconds(self) -> float:
        """Return the total time span in milliseconds."""
        return self._seconds / TimeEnum.NanoSecond.value
    
    @property
    def TotalMicroSeconds(self) -> float:
        """Return the total time span in milliseconds."""
        return self._seconds / TimeEnum.MicroSecond.value
    
    @property
    def TotalMilliSeconds(self) -> float:
        """Return the total time span in milliseconds."""
        return self._seconds / TimeEnum.MilliSecond.value
    
    @property
    def TotalSeconds(self) -> float:
        """Return the total time span in Seconds."""
        return self._seconds

    @property 
    def TotalMinutes(self) -> float:
        """Return the total time span in minutes."""
        return self._seconds / TimeEnum.Minute.value
    
    @property
    def TotalHours(self) -> float:
        """Return the total time span in hours."""
        return self._seconds / TimeEnum.Hour.value
    
    @property
    def TotalDays(self) -> float:
        """Return the total time span in days."""
        return self._seconds / TimeEnum.Day.value
    
    @property
    def TotalWeeks(self) -> float:
        """Return the total time span in weeks."""
        return self._seconds / TimeEnum.Week.value

    @property
    def NanoSeconds(self):
        # uses direct string cutting to avoid floating precision errors, eg 86400.0011 % 1 does not return 0.0011 but instead 0.00109999...
        seconds_decimals = Decimal(str(self._seconds)) % Decimal('1')
        milliseconds_asInt = seconds_decimals * Decimal('1000')
        milliseconds_decimals = Decimal(milliseconds_asInt) % Decimal('1')
        microseconds_asInt = milliseconds_decimals * Decimal('1000')
        microseconds_decimals = Decimal(microseconds_asInt) % Decimal('1')
        nanoseconds_asInt = microseconds_decimals * Decimal('1000')
        return int(nanoseconds_asInt)
        
    @property
    def MicroSeconds(self):
        # uses direct string cutting to avoid floating precision errors, eg 86400.0011 % 1 does not return 0.0011 but instead 0.00109999...
        seconds_decimals = Decimal(str(self._seconds)) % Decimal('1')
        milliseconds_asInt = seconds_decimals * Decimal('1000')
        milliseconds_decimals = Decimal(milliseconds_asInt) % Decimal('1')
        microseconds_asInt = milliseconds_decimals * Decimal('1000')
        return int(microseconds_asInt)
    @property
    def MilliSeconds(self):
        # uses direct string cutting to avoid floating precision errors, eg 86400.0011 % 1 does not return 0.0011 but instead 0.00109999...
        seconds_decimals = Decimal(str(self._seconds)) % Decimal('1')
        milliseconds_asInt = seconds_decimals * Decimal('1000')
        return int(milliseconds_asInt)

    @property
    def Seconds(self):
        return int(self._seconds % 60)

    @property
    def Minutes(self):
        return int((self._seconds / TimeEnum.Minute.value) % 60)

    @property
    def Hours(self):
        return int((self._seconds / TimeEnum.Hour.value) % 24)

    @property
    def Days(self):
        return int((self._seconds / TimeEnum.Day.value) % 7)
    
    @property
    def Weeks(self):
        return int(self._seconds / TimeEnum.Week.value)
    
    def Partition(self, minUnit:TimeEnum=None, maxUnit:TimeEnum=None) -> dict[TimeEnum, float]:
        """Splits the current timespan to individual parts

        :param minUnit: The smallest part that should be included in the resulting dict. \
            if there are smaller parts available than minUnit, they will be added as decimals to minUnit 
        :param maxUnit:  The highest part that should be included in the resulting dict. \
            If there are bigger parts available than maxUnit, they will be added as the maxUnit unit instead.
            This implies that when maxUnit is specified to say hours, in the case \
            that there is 1 complete day, it will instead be added to hours as 24
        :return: dictionary of all used enums as keys, and their corresponding amount as values

        Example Usage:

        >>> TimeSpan(seconds=30, minutes=2).Partition()
        {
            TimeEnum.NanoSeconds: 0.0,
            TimeEnum.MicroSeconds: 0.0,
            TimeEnum.MilliSeconds: 0.0,
            TimeEnum.Seconds: 30.0,
            TimeEnum.Minute: 2.0,
            TimeEnum.Hour: 0.0,
            TimeEnum.Day: 0.0,
            TimeEnum.Week: 0.0,
        }
        >>> TimeSpan(days=1).Partition(maxUnit=TimeEnum.Hour)
        {
            TimeEnum.NanoSeconds: 0.0,
            TimeEnum.MicroSeconds: 0.0,
            TimeEnum.MilliSeconds: 0.0,
            TimeEnum.Seconds: 0.0,
            TimeEnum.Minute: 0.0,
            TimeEnum.Hour: 24.0,
        }
        >>> TimeSpan(seconds=1, hours=1, milliseconds=100).Partition(minUnit=TimeEnum.Second, maxUnit=TimeEnum.Minute)
        {
            TimeEnum.Seconds: 1.1,
            TimeEnum.Minute: 60.0,
        }

        """

        #we will use decimals to mitigate floating issues when using modulo/division operations
        #this is because small rounding issues can be amplified with noisy decimals and can make incorrect partition
        #results mainly on very small units

        parts = {}
        remaining = Decimal(str(self._seconds))

        # list time units descending to get biggest parts to smallest
        descendingUnits = [
            TimeEnum.Week,
            TimeEnum.Day,
            TimeEnum.Hour,
            TimeEnum.Minute,
            TimeEnum.Second,
            TimeEnum.MilliSecond,
            TimeEnum.MicroSecond,
            TimeEnum.NanoSecond,
        ]
        for enumUnit in descendingUnits:
            if maxUnit and (enumUnit.value > maxUnit.value):
                continue
            
            preciseEnumUnitValue = Decimal(str(enumUnit.value))
            if enumUnit.value <= remaining:
                part = remaining // preciseEnumUnitValue
                parts[enumUnit] = float(part)
                remaining %= preciseEnumUnitValue
            else:
                parts[enumUnit] = 0.0
            
            if minUnit and (minUnit == enumUnit):
                break
        
        #gather the leftovers to the smallest part if any
        if(remaining > 0):
            #use last TimeSpan in loop since that will be the smallest part
            parts[enumUnit] = parts[enumUnit] + float(remaining / preciseEnumUnitValue)
        return parts
    
   #region archimetric overloading
    def __eq__(self, other):
        if isinstance(other, TimeSpan):
            return self._seconds == other._seconds
        return False
    
    def __lt__(self, other:'TimeSpan'):
        #lower than operator
        if not isinstance(other, TimeSpan):
            raise TypeError("Unsupported operand type(s) for <")
        
        return self._seconds < other._seconds
    
    def __le__(self, other:'TimeSpan'):
        # lower than or equal operator

        if not isinstance(other, TimeSpan):
            raise TypeError("Unsupported operand type(s) for <=")

        return self._seconds <= other._seconds
    
    def __gt__(self, other:'TimeSpan'):
        # greater than operator

        if not isinstance(other, TimeSpan):
            raise TypeError("Unsupported operand type(s) for >")

        return self._seconds > other._seconds
    
    def __ge__(self, other:'TimeSpan'):
        # greater than or equal operator

        if not isinstance(other, TimeSpan):
            raise TypeError("Unsupported operand type(s) for >=")

        return self._seconds >= other._seconds


    def __add__(self, other:'TimeSpan') -> 'TimeSpan':
        '''addition of two timespans, returns a new independent timespan object'''
        if not isinstance(other, TimeSpan):
            raise TypeError("Unsupported operand type(s) for +")
        
        total_seconds = self._seconds + other._seconds
        return TimeSpan(seconds=total_seconds)

    def __iadd__(self, other: 'TimeSpan') -> 'TimeSpan':
        '''inplace addition of another timespan'''
        if not isinstance(other, TimeSpan):
            raise TypeError("Unsupported operand type(s) for TimeSpan.Add")
        self._seconds += other._seconds
        return self

    def __sub__(self, other:'TimeSpan') -> 'TimeSpan':
        '''subtraction of two timespans, returns a new independent timespan object'''
        if not isinstance(other, TimeSpan):
            raise TypeError("Unsupported operand type(s) for +")
        
        total_seconds = self._seconds - other._seconds
        return TimeSpan(seconds=total_seconds)

    def __isub__(self, other: 'TimeSpan') -> 'TimeSpan':
        '''inplace subtraction of another timespan'''
        if not isinstance(other, TimeSpan):
            raise TypeError("Unsupported operand type(s) for TimeSpan.Subtract")
        self._seconds -= other._seconds
        return self
    #endregion archimetric overloading
