FROM haproxy
COPY haproxy2.cfg /usr/local/etc/haproxy/haproxy.cfg
RUN groupadd -r haproxy && useradd -r -g haproxy haproxy

COPY errors/400.http /etc/haproxy/errors/400.http
COPY errors/403.http /etc/haproxy/errors/403.http
COPY errors/408.http /etc/haproxy/errors/408.http
COPY errors/500.http /etc/haproxy/errors/500.http
COPY errors/502.http /etc/haproxy/errors/502.http
COPY errors/503.http /etc/haproxy/errors/503.http
COPY errors/504.http /etc/haproxy/errors/504.http
