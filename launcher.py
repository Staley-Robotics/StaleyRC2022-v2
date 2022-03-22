import ctre
import wpilib

class Launcher:

    def __init__(self):
        self.intake_toggle: bool = False
        self.high_shot_timestamp = None
        self.low_shot_timestamp = None
        self.shooter = ctre.WPI_TalonFX(5, "rio")
        self.barrel = ctre.WPI_VictorSPX(6)
        self.storage = ctre.WPI_VictorSPX(7)
        self.intake = ctre.WPI_VictorSPX(8)

    def update(self, time: float, controller: wpilib.XboxController):
        if controller.getRightBumper():
            self.intake_toggle = not self.intake_toggle
        self.intake.set(float(self.intake_toggle))
        self.storage.set(float(self.intake_toggle))
        self.shooter.set(controller.getRightTriggerAxis())
        if self.high_shot_timestamp < time and self.high_shot_timestamp + 3 > time:
            self.shooter.set(0.75)
        else:
            self.shooter.set(0)
        if self.low_shot_timestamp < time and self.low_shot_timestamp + 3 > time:
            self.shooter.set(0.4)
        else:
            self.shooter.set(0)
        if self.high_shot_timestamp + 2 < time and self.high_shot_timestamp + 3 > time:
            self.barrel.set(0.5)
        else:
            self.barrel.set(0)
        if self.low_shot_timestamp + 2 < time and self.low_shot_timestamp + 3 > time:
            self.barrel.set(0.5)
        else:
            self.barrel.set(0)
        if controller.getXButtonPressed():
            self.low_shot_timestamp = time
        elif controller.getBButtonPressed():
            self.low_shot_timestamp = time
        elif controller.getYButton():
            self.barrel.set(0.5)
        else:
            self.barrel.set(0.0)
