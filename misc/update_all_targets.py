from requests import Session

session = Session()

asu_url = "http://srvfedora2.ourhome.co.za:8100"


def reload_all():
    versions = session.get("https://downloads.openwrt.org/.versions.json").json()[
        "versions_list"
    ]
    for version in versions:
      if version == "23.05.4":
        print(f"Reloading {version}")
        targets = session.get(
            f"https://downloads.openwrt.org/releases/{version}/.targets.json"
        )
        if targets.status_code == 404:
            print(f"Targets not found for {version}")
            continue
        targets = targets.json()
        for target in targets:
          if target == "ipq40xx/mikrotik":
            print(f"Reloading {version}/{target}")
            session.get(
                f"{asu_url}/api/v1/update/{version}/{target}",
                headers={"X-Update-Token": "changeme"},
            )

#    targets = session.get(
#        "https://downloads.openwrt.org/snapshots/.targets.json"
#    ).json()
#    for target in targets:
#        print(f"Reloading SNAPSHOT/{target}")
#        session.get(
#            f"{asu_url}/api/v1/update/SNAPSHOT/{target}",
#            headers={"X-Update-Token": "changeme"},
#        )


reload_all()
