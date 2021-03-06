#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Created by eeliu at 8/20/20

# ******************************************************************************
#   Copyright  2020. NAVER Corp.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
# ******************************************************************************

def monkey_patch():

    from pinpoint.common import Interceptor
    try:
        import pymongo
        from .MongoClientPlugin import MongoClientPlugin

        Interceptors = [
            Interceptor(pymongo.collection,'find', MongoClientPlugin),
            Interceptor(pymongo.collection, 'insert', MongoClientPlugin),
            Interceptor(pymongo.collection, 'update', MongoClientPlugin),
            Interceptor(pymongo.collection, 'update_many', MongoClientPlugin),
            Interceptor(pymongo.collection, 'delete_one', MongoClientPlugin),
            Interceptor(pymongo.collection, 'delete_many', MongoClientPlugin),
            Interceptor(pymongo.collection, 'insert_many', MongoClientPlugin),
            Interceptor(pymongo.collection, 'insert_one', MongoClientPlugin),
        ]

        for interceptor in Interceptors:
            interceptor.enable()

    except ImportError:
        pass



__all__=['monkey_patch']

