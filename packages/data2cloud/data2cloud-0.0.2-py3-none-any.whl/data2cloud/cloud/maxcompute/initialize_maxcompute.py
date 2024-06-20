import json
import os
import subprocess
from odps import ODPS
from odps.inter import setup, enter, teardown, list_rooms


class _MaxcomputeSetup:
    def __init__(self):
        self.default_project = "dteam_dw_dev"
        self.endpoint = "http://service.cn-zhangjiakou.maxcompute.aliyun.com/api"

    def _setup(self):
        if self._inited:
            return

        # way 1: read aliyun config by command line *=(default profile only)
        script = "aliyun configure get --profile default"
        result = subprocess.run(
            [script],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True,
        )
        config = json.loads(result.stdout)
        access_key_id = config["access_key_id"]  # type: ignore
        access_key_secret = config["access_key_secret"]  # type: ignore

        ## way 2: read aliyun config's current profile, need pip install alibabacloud_tea_openapi
        # from alibabacloud_credentials.client import Client as CredClient
        # from alibabacloud_tea_openapi.models import Config
        # home_dir = os.path.expanduser("~")
        # config_file = os.path.join(home_dir, ".aliyun/config.json")
        # aliyun_config = json.load(open(config_file))
        # config_info = [
        #     x for x in aliyun_config["profiles"] if x["name"] == aliyun_config["current"]
        # ][0]
        # config = Config(
        #     config_info["access_key_id"],
        #     config_info["access_key_secret"],
        #     type="access_key",
        #     region_id=config_info["region_id"],
        # )
        # cred = CredClient(config)
        # access_key_id = cred.get_access_key_id()
        # access_key_secret = cred.get_access_key_secret()

        # https://pyodps.readthedocs.io/zh-cn/stable/interactive.html
        # setup后, 任何地方均可以使用, 通过以下代码获得odps实例
        # ```
        # room = enter()
        # o = room.odps
        # ```

        teardown()
        setup(
            access_key_id,
            access_key_secret,
            self.default_project,
            endpoint=self.endpoint,
        )

    @property
    def _inited(self):
        rooms = list_rooms()
        if len(rooms) == 0:
            return False
        return True

    @property
    def default_odps(self) -> ODPS:
        self._setup()
        return enter().odps
