# Custom installation

<ol>
    <li>Fedora Server 40</li>
    <li>Docker using Portainer</li>
    <li>Podman to build</li>
</ol>

## Files changed or added:<br>

<ol>
    <li>asu/config.py</li>
        - On my linux I stored all container content in /opt/asu<br>
        - Change public_path to allow for /opt/asu<br>
        - Not required but changed redis_url<br>
        - Set update_token to code version<br>
        - Not required but change log_level<br>
    <li>asu/main.py</li>
        - When not using HTTPS and NGINX I had to make two changes<br>
        - Allow CORS<br>
        - Change routing allowing /api<br>
    <li>misc/update_all_targets.py</li>
        - Specify my host asu_url<br>
        - Limit to specific version and target with if<br>
        - Removed snapshots, commented out<br>
    <li>portainer-stack</li>
        - Used in Portainer to create the asu stack using the pre-build container on Docker Hub<br>
        - Mapping in config.py and main.py<br>
        - Map in /opt/asu<br>
        - Set container_host to Fedora's<br>
</ol>

## Changes on Fedora
`dnf install podman`<br>
`dnf install podman-compose`<br>
`reboot`<br>

### Verify<br>

![Podman API Service](podman-api-service.png)

![Podman API Socket](podman-api-socket.png)

## Chrome and mixed content

https://stackoverflow.com/questions/73875589/disable-website-redirection-to-https-on-chrome

Only solution that worked for me <i>(trust me I tried it all)</i>

Go to `chrome://settings/content/insecureContent` , add your website/router pattern under Allowed to show insecure content

### Example:

`[*.]demo.com`

### Additional Chrome checks

#### hsts
Type in: `chrome://net-internals/#hsts` in address bar of chrome. At the bottom place the domain to delete from HSTS.

#### Always use secure connections
Under: Settings -> Privacy and Security -> Security I found this toggle which I disabled: enter image description here

![alt text](chrome-setting.png)

#### Sites settings
Click the lock in the browser address bar opposite the domain name<br>
Select `Site Settings`<br>
Click `Clear Data` against `cookies`<br>
Then scroll down to `Insecure content` and click `Allow`<br>