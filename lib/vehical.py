import math

class Vector2:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self,other):
        return Vector2(self.x - other.x, self.y - other.y)
    
    def __mul__(self,other):
        if not isinstance(other,Vector2):
            self.x *= other
            self.y *= other
            return Vector2(self.x, self.y)
        elif isinstance(other,Vector2):
            self.x *= other.x
            self.y *= other.y
            return self.x + self.y
        else:
            pass

        
    
    def __div__(self,other):
        if not isinstance(other, Vector2):
            self.x /= other
            self.y /= other
        else:
            pass
    
        return Vector2(self.x, self.y)


    def length(self):
        return math.sqrt(self.x*self.x + self.y*self.y)
    
    def normalize(self):
        return Vector2(self.x/self.length(), self.y/self.length())

class vehical:
    def __init__(self, mass=2000):
        self.mass = mass

        self.x = 1
        self.y = 1
        self.vx = 1
        self.vy = 1
        self.ax = 0
        self.ay = 0
        self.fx = 0
        self.fy = 0

        self.slope = 0
        self.body_torque = 0
        self.body_angular_accel = 0
        self.body_angular_velocity = 0
        self.body_angular_position = 0

        self.throttle = 0
        self.braking = 0
        self.steering = 0
        self.gear = 1

        self.F_d = 0
        self.F_r = 0
        self.F_g = 0
        self.F_t = 0
        self.F_b = 0

        self.C_d = 0.2
        self.C_r = 0.2
        self.C_b = 0.2
        self.C_a = 0.2
        self.g = 9.8

        self.B = 0.5
        self.C = 0.5
        self.H = 0.2
        self.L = self.B + self.C
        self.W = self.mass * self.g

        self.front_load = (self.C / self.L) * self.W
        self.rear_load = (self.B / self.L) * self.W

        self.Wheel_torque = 0
        self.Wheel_radius = 0.5
        self.Alpha_front = 0
        self.Alpha_rear = 0
        self.Beta = 0

        self.rpm = 0
        self.redline = 12000
        self.gears = [-0.2, 0.000001, 0.2, 0.4, 0.8, 1.6, 2]
        self.final_gear_drive = 0.38
        
        self.V = Vector2(self.vx, self.vy)
        self.DIR = Vector2(self.x, self.y)

        self.sgn = lambda x: -1 if x < 0 else 1 if x > 0 else 0
        
    def update_position(self):
        self.ax = self.fx / self.mass
        self.ay = self.fy / self.mass
        self.vx += self.ax * self.dt
        self.vy += self.ay * self.dt
        self.x += self.vx * self.dt
        self.y += self.vy * self.dt

    def update_force(self):
        self.F_d = Vector2(-self.C_d * self.V.x * abs(self.V.x), -self.C_d * self.V.y * abs(self.V.y))
        self.F_r = Vector2(-self.C_r * self.V.x, -self.C_r * self.V.y)
        self.F_g = self.mass * self.g * math.sin(self.slope)
        self.F_t = self.Wheel_torque / self.Wheel_radius * self.throttle
        self.F_b = -self.sgn(self.V.x) * self.C_b * self.braking

        self.F = self.F_d + self.F_r 
        self.fx = self.F_t + self.F_lat_front *math.sin(self.steering) * self.F.x
        self.fy = self.F_lat_rear + self.F_lat_front * math.cos(self.steering) * self.F.y

    def update_engine(self):
        self.rpm = (self.vx * (60 * self.gears[self.gear] * self.final_gear_drive) / (math.tau * self.Wheel_radius)) + 1000
        engine_torque_map = lambda : (((0*(min(self.rpm, self.redline) ** 2)) + (0 * min(self.rpm, self.redline)) + 0) * (math.tau)) / 60
        self.Wheel_torque = engine_torque_map() * self.gears[self.gear] * self.final_gear_drive
        self.Wheel_speed = (math.tau * self.rpm) / (60 * self.gears[self.gear] * self.final_gear_drive)

    def update_gear(self):
        pass

    def update_wheel(self):
        self.Beta = math.acos((self.V * self.DIR) / (self.V.length() * self.DIR.length()))
        self.Alpha_front = math.atan((self.vx + self.body_angular_velocity * self.B) / self.vy) - self.steering * self.sgn(self.vy)
        self.Alpha_rear = math.atan((self.vx + self.body_angular_velocity * self.C) / self.vy)

        self.F_lat_front = self.C_a * self.Alpha_front * self.front_load * 0.5
        self.F_lat_rear = self.C_a * self.Alpha_rear * self.rear_load * 0.5

        self.body_torque = math.cos(self.steering) * ((self.F_lat_front * self.B) - (self.F_lat_rear * self.C))
        self.body_angular_accel = self.body_torque / self.mass
        self.body_angular_velocity += self.body_angular_accel * self.dt  
        self.body_angular_position += self.body_angular_velocity * self.dt

    def update_body(self):
        pass

    def update(self, dt, throttle=0, braking=0, gear=1):
        self.dt = dt
        self.throttle = throttle
        self.braking = braking
        self.gear = gear

        self.V = Vector2(self.vx, self.vy)
        self.DIR = Vector2(self.x, self.y)

        self.update_wheel()
        self.update_engine()
        self.update_gear()
        self.update_force()

if __name__ == "__main__":
    test = vehical()