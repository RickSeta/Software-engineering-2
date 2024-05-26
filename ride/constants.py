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
    RideStatus.SCHEDULED.value: RideStatusDisplayName.SCHEDULED.value,
    RideStatus.IN_PROGRESS.value: RideStatusDisplayName.IN_PROGRESS.value,
    RideStatus.COMPLETED.value: RideStatusDisplayName.COMPLETED.value,
    RideStatus.CANCELLED.value: RideStatusDisplayName.CANCELLED.value,
}
