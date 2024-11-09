# import docker
# from docker.errors import ImageNotFound, APIError
#
# client = docker.from_env()
#
#
# def get_image_info(image_name: str):
#     """
#
#      {'
#      client': <docker.client.DockerClient object at 0x7fa628769d80>,
#     'collection': <docker.models.images.ImageCollectionobject at 0x7fa6282baf20>,
#     'attrs':
#             {
#                 'Id': 'sha256:ab363ab21d7b44b4b0c4032655dca5e812153e81966e758fcdb08cef9d0159e2',
#                 'RepoTags': ['python:latest'],
#                 'RepoDigests':
#                   ['python@sha256:4584ea46d313a10e849eb7c5ef36be14773418233516ceaa9e52a8ff7d5e35a5'],
#                 'Parent': '',
#                 'Comment': 'buildkit.dockerfile.v0',
#                 'Created': '2024-06-07T03:53:24Z',
#                 'ContainerConfig':
#                          {
#                             'Hostname': '',
#                             'Domainname': '',
#                             'User': '',
#                             'AttachStdin': False,
#                             'AttachStdout': False,
#                             'AttachStderr': False,
#                             'Tty': False,
#                             'OpenStdin': False,
#                             'StdinOnce': False,
#                             'Env': None,
#                             'Cmd': None,
#                             'Image': '',
#                             'Volumes': None,
#                             'WorkingDir': '',
#                             'Entrypoint': None,
#                             'OnBuild': None,
#                             'Labels': None
#                          },
#
#                 'DockerVersion': '',
#                 'Author': '',
#                 'Config':
#                                   {
#                                   'Hostname': '',
#                                    'Domainname': '',
#                                     'User': '',
#                                     'AttachStdin': False,
#                                     'AttachStdout': False,
#                                     'AttachStderr': False,
#                                     'Tty': False,
#                                     'OpenStdin': False,
#                                     'StdinOnce': False,
#                                     'Env':
#                                             [
#                                             'PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
#                                              'LANG=C.UTF-8', 'GPG_KEY=7169605F62C751356D054A26A821E680E5FA6305',
#                                               'PYTHON_VERSION=3.12.4',
#                                                'PYTHON_PIP_VERSION=24.0',
#                                                 'PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/dbf0c85f76fb6e1ab42aa672ffca6f0a675d9ee4/public/get-pip.py',
#                                                  'PYTHON_GET_PIP_SHA256=dfe9fd5c28dc98b5ac17979a953ea550cec37ae1b47a5116007395bfacff2ab9'
#                                                  ],
#                                     'Cmd': ['python3'],
#                                     'ArgsEscaped': True,
#                                     'Image': '',
#                                     'Volumes': None,
#                                     'WorkingDir': '',
#                                     'Entrypoint': None,
#                                     'OnBuild': None,
#                                     'Labels': None
#                                   },
#                 'Architecture': 'amd64',
#                 'Os': 'linux',
#                 'Size': 1018840040,
#                 GraphDriver':
#                                 {
#                                     'Data':
#                                         {
#                                         'LowerDir': '/var/lib/docker/overlay2/c7f00335b851037a1b375e95ca0a93ee867e45ed66c9e822de42aa825da39f7a/diff:/var/lib/docker/overlay2/ccac443990644fc72b5eab7f74c
#                                         d2a3161c6ad1198b8cc2ba633e40c2d7c306d/diff:/var/lib/docker/overlay2/5f121e2deecfe101d471569d84ad398b051e092ff6e388a1bd7c370fab1e543b/diff:/var/lib/docke
#                                         r/overlay2/3520e690d8360ef39e859f6cc0e90e0fa81c3134b678a434316f6cf883ae47a3/diff:/var/lib/docker/overlay2/b1433a7da4e800f07657525c958c03f23f0fd4365a16af
#                                         2989af986249cd20b8/diff:/var/lib/docker/overlay2/29d33c239e3dbc86d68ef618b4d9df0fa2c27e9dfd1143a83d0a5a915c5a2dd8/diff:/var/lib/docker/overlay2/0ebcfb47
#                                         4e551b9f4138fa28b210a3976601a36ee56077b631ac0191258a8723/diff',
#                                          'MergedDir': '/var/lib/docker/overlay2/c552f5ac5b7b07ef9aa214be2979789b112310a9c90ea0620755c9f480bf2ae8/merged',
#                                           'UpperDir': '/var/lib/docker/overlay2/c552f5ac5b7b07ef9aa214be2979789b112310a9c90ea0620755c9f480bf2ae8/diff',
#                                            'WorkDir': '/var/lib/docker/overlay2/c552f5ac5b7b07ef9aa214be2979789b112310a9c90ea0620755c9f480bf2ae8/work'
#                                            },
#                                     'Name': 'overlay2'
#                                 },
#                 'RootFS':
#                     {
#                         'Type': 'layers',
#                          'Layers':[
#                             'sha256:5d64de483bf527bb00d0d2749f8b2b2b21c101e32e6a6be715b7f6c8eae5496b',
#                              'sha256:d3e8d42f967c9c00049f90237e1bf4a460d18c28895292d2bb4a0702f661a745',
#                                 'sha256:43df359389fd238ca1dd17ce5c385d76a0c601114428f00bbb736899a5533756',
#                                  'sha256:3999ea91fb6e02b28a29310ba7591e310203a1a5a96360dbea8814fb52f2b870',
#                                   'sha256:b13fdecc2461a8dedb0677f5800c5bbd3a578ace8a8884ca4b9f8bcff3283dbe',
#                                    'sha256:9f8b33471be3c420140a1783d8f76db27fda40221376008ad397277ac619ca69',
#                                     'sha256:b3bd104b86dbf0def3539f3c697207208d50ee63fd8a6ad1e8690d4d94415f67',
#                                      'sha256:5676027ddc89bd2fa0b1360ff0098d8880ab9139a931298c248a916d6e1c70d5'
#                                      ]
#                     },
#                 'Metadata': {'LastTagTime': '0001-01-01T00:00:00Z'}, 'Container': ''}
#             }
#
#
#
#     :param image_name:
#     :return:
#     """
#     try:
#         image = client.images.get(image_name)
#         # print("+++++++++++++++++++++++++++++++++", image.__dict__)
#         return {
#             "id": image.id,
#             "tags": image.tags,
#             "created": image.attrs['Created'],
#             "size": image.attrs['Size'],
#             # "collection": image.collection,
#             "RepoDigests": image.attrs['RepoDigests'],
#             "Architecture": image.attrs['Architecture'],
#             "OS": image.attrs['Os'],
#             "labels": image.attrs['Config']['Labels'],
#             "Metadata": image.attrs['Metadata']
#         }
#     except ImageNotFound:
#         try:
#             # Attempt to pull the image if it does not exist locally
#             print(f"Image {image_name} not found locally. Attempting to pull from Docker registry...")
#             image = client.images.pull(image_name)
#
#             print("++++++++++++++++++++++++++++++++++++++++++++++++++++", image.__dict__)
#             return {
#                 "id": image.id,
#                 "tags": image.tags,
#                 # "collection": image.collection,
#                 # "client": image.client,
#                 "OS": image.attrs['Os'],
#                 "RepoDigests": image.attrs['RepoDigests'],
#                 "created": image.attrs['Created'],
#                 "size": image.attrs['Size'],
#                 "Architecture": image.attrs['Architecture'],
#                 "labels": image.attrs['Config']['Labels'],
#                 "Metadata": image.attrs['Metadata']
#             }
#         except APIError as e:
#             return {"error": f"Image {image_name} not found and could not be pulled: {str(e)}"}
#     except APIError as e:
#         return {"error": f"Error retrieving image info: {str(e)}"}
#     except Exception as e:
#         return {"error": f"An unexpected error occurred: {str(e)}"}
