import secure
from secure.headers import XFrameOptions, XXSSProtection

server = secure.Server().set("Secure")

csp = (
    secure.ContentSecurityPolicy()
    .default_src("'none'")
    .base_uri("'self' 'https:'")
    .script_src("'self")
    .style_src("'self")
    .connect_src("'self'")
    .frame_src("'none'")
    .img_src("'self'")
    .frame_ancestors("'none")
)

hsts = secure.StrictTransportSecurity().include_subdomains().preload().max_age(31536000)

referrer = secure.ReferrerPolicy().strict_origin_when_cross_origin()

permissions_value = (
    secure.PermissionsPolicy()
    .geolocation("self")
    .vibrate()
    .microphone("none")
    .usb("none")
    .camera("none")
    .magnetometer("none")
    .accelerometer("none")
)

cache_value = secure.CacheControl().no_cache().no_store().no_transform()

feature = "accelerometer ‘none’; camera ‘none’; geolocation ‘none’; gyroscope ‘none’; magnetometer ‘none’; microphone ‘none’; payment ‘none’; usb ‘none’"

# xfo = XFrameOptions.sameorigin("self",)

xss = secure.XXSSProtection().set("1; mode=block")
# debug(xss)
secure_headers = secure.Secure(
    server=server,
    csp=csp,
    hsts=hsts,
    referrer=referrer,
    permissions=permissions_value,
    cache=cache_value,
    xxp=xss
    # xfo=xfo
    # feature=feature
)
