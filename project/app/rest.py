from flask_restful import Resource
from flask import request
from flask.ext.restful import abort

from model import db


def row2dict(row):
    d = {}
    table = str(row._sa_instance_state.class_._table)
    for column in row._sa_instance_state.class_._table.columns:
        col = column.name.replace(table + '.', '')
        d[col] = str(getattr(row, col))
    return d


def rows2dict(rows):
    arr = []
    if (len(rows) < 1):
        return arr

    table = str(rows[0]._sa_instance_state.class_._table)
    columns = rows[0]._sa_instance_state.class_._table.columns
    for r in rows:
        d = {}
        for column in columns:
            col = column.name.replace(table + '.', '')
            d[col] = str(getattr(r, col))
        arr.append(d)
    return arr


class Base(Resource):
    def get(self, key_id):
        try:
            entity = self.get_entity()
            user = entity.filter(entity.nid == key_id).one()
            return row2dict(user)
        except Exception as e:
            abort(500, message=str(e))


class BaseList(Resource):
    def get(self):
        try:
            args = request.args
            sqa_args = {}
            for a in args:
                sqa_args[a] = args[a]

            if (len(args) == 0):
                user = self.get_entity().all()
            else:
                user = self.get_entity().filter_by(**(sqa_args)).all()
            return rows2dict(user)
        except Exception as e:
            abort(500, message=str(e))

    def post(self):
        try:
            data = request.json
            entity = self.get_entity()
            user = entity.insert(**(data))
            db.commit()
            return row2dict(user)
        except Exception as e:
            db.rollback()
            abort(500, message=str(e))


class Users(Base):
    def get_entity(self):
        return db.users


class UsersList(BaseList):
    def get_entity(self):
        return db.users

    def get(self):
        try:
            args = request.args
            sqa_args = {}
            vehicles_filter = {}
            # this parts takes care of transforming
            # parameters in sqlalchemy friendly dicts
            for a in args:
                if ('vehicles' in a):
                    vehicles_filter[a.split('.')[1]] = args[a]
                    continue

                sqa_args[a] = args[a]

            # if there is "composite" filter
            if (len(vehicles_filter) > 0):
                user = db.users.filter_by(**(sqa_args)). \
                    join(db.users.objects). \
                    filter_by(**(vehicles_filter)).all()
            elif (len(args) == 0):
                user = db.users.all()
            else:
                user = db.users.filter_by(**(sqa_args)).all()
            return rows2dict(user)
        except Exception as e:
            abort(500, message=str(e))

    def post(self):
        try:
            data = request.json
            vehicles = ''
            # only one relation can be set on creation
            if ('vehicles' in data):
                vehicles = int(data['vehicles'])
                del data['vehicles']

            user = db.users.insert(**(data))
            if (vehicles != ''):
                v = db.objects.filter(db.objects.nid == vehicles).first()
                user.objects.append(v)
            db.commit()
            return row2dict(user)
        except Exception as e:
            db.rollback()
            abort(500, message=str(e))


class Vehicles(Base):
    def get_entity(self):
        return db.objects


class VehiclesList(BaseList):
    def get_entity(self):
        return db.objects

    def get(self):
        try:
            args = request.args
            sqa_args = {}
            user_filter = {}
            for a in args:
                if ('users' in a):
                    user_filter[a.split('.')[1]] = args[a]
                    continue
                sqa_args[a] = args[a]

            if (len(user_filter) > 0):
                user = db.objects.filter_by(**(sqa_args)). \
                    join(db.objects.users). \
                    filter_by(**(user_filter)).all()
            elif (len(args) == 0):
                user = db.objects.all()
            else:
                user = db.objects.filter_by(**(sqa_args)).all()
            return rows2dict(user)
        except Exception as e:
            abort(500, message=str(e))

    def post(self):
        try:
            data = request.json
            entity = self.get_entity()
            users = ''
            # only one relation can be set on creation
            if ('users' in data):
                users = int(data['users'])
                del data['users']

            vehicle = entity.insert(**(data))

            if (users != ''):
                u = db.users.filter(db.users.nid == users).first()
                vehicle.users.append(u)
            db.commit()
            return row2dict(vehicle)
        except Exception as e:
            db.rollback()
            abort(500, message=str(e))


class Locations(Base):
    def get_entity(self):
        return db.locations


class LocationsList(BaseList):
    def get_entity(self):
        return db.objects


class Settings(Base):
    def get_entity(self):
        return db.settings


class SettingsList(Base):
    def get_entity(self):
        return db.settings


class Providers(Base):
    def get_entity(self):
        return db.providers


class ProvidersList(BaseList):
    def get_entity(self):
        return db.providers
