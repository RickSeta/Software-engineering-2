from enum import Enum


class RideStatus(Enum):
    SCHEDULED = 'scheduled'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'


class RideStatusDisplayName(Enum):
    SCHEDULED = 'Agendada'
    IN_PROGRESS = 'Em andamento'
    COMPLETED = 'Finalizada'
    CANCELLED = 'Cancelada'


RIDE_STATUS_DISPLAY_NAME = {
    RideStatus.SCHEDULED: RideStatusDisplayName.SCHEDULED,
    RideStatus.IN_PROGRESS: RideStatusDisplayName.IN_PROGRESS,
    RideStatus.COMPLETED: RideStatusDisplayName.COMPLETED,
    RideStatus.CANCELLED: RideStatusDisplayName.CANCELLED,
}
