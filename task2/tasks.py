from logger_module import *
import data_helper as data
import time

class MovementTask():
    
    def __init__(self, uid, bot, move_points, info=''):
        self.uid = uid
        self.status = 'still'
        self.bot = bot
        path = []
        for p in move_points:
            points = p.split(' ')
            path.append(points)
        self.point_path = path
        self.info = info

    def __process__(self):
        self.move()

    def move(self):
        logger.debug('%s Start Moving...' % (self.bot.name))
        self.status = 'moving'
        for point in self.point_path:
            logger.debug('%s New bot position: %s'  % (self.bot.name, str(point)))
            self.bot.point['x'] = self.bot.gun_point['x'] = point[0]
            self.bot.point['y'] = self.bot.gun_point['y'] = point[1]
            self.bot.point['z'] = self.bot.gun_point['z'] = point[2]
        logger.debug('%s Finish moving at position: %s' % (self.bot.name, str(self.point_path[-1])))

    def teleport(self, x, y, z):
        self.status = 'teleport'
        logger.debug('Teleport bot %s on position: %s %s %s' % (self.bot.name, x, y, z))
        self.bot.point['x'] = x
        self.bot.point['y'] = y
        self.bot.point['z'] = z
        self.status = 'stil'

class ShootTask():

    def __init__(self, *args, **kwargs):
        self.uid = kwargs['uid']
        self.bot = kwargs['bot']
        self.target = kwargs['target_position'].split(' ')
        self.ammo_type = kwargs['ammo']
        self.reload = kwargs['reload_time']
        self.shots = kwargs['shotsToKill']
        self.info = kwargs.get('info', 'ShootTask #' + str(self.uid))

    def __process__(self):
        self.shoot_at_target()

    def shoot_at_target(self):
        logger.info('%s Start shoothing at %s by %s shells' % (self.bot.name, self.target, self.ammo_type))
        if list(set(self.bot.gun_point) & set(self.target)) == []:
            self.status = 'aiming'
            self.bot.gun_point['x'] = self.target[0]
            self.bot.gun_point['y'] = self.target[1]
            self.bot.gun_point['z'] = self.target[2]
            # wait for turret move on target
            time.sleep(2)

        for shots_count in range(1, self.shots+1):
            self.status = 'shooting'
            logger.debug('%s, %s shot #%s' % (self.bot.name, self.ammo_type, str(shots_count)))
            self.shoot(self.ammo_type)
            self.status = 'reloading'
            time.sleep(self.reload)
            self.status = 'ready'

    def shoot(self, ammo_type):
        print data.test_data['shots_types'][str(ammo_type)]
           
