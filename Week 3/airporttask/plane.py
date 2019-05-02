from aircraft import Aircraft

class Plane(Aircraft):

    def _init_(self, plane_id):
        super()._init_()
        self.plane_id=plane_id

plane_1 = Plane('model 1')
plane_2 = Plane('model 2')
plane_3 = Plane('model 3')
plane_4 = Plane('model 4')
plane_5 = Plane('model 5')