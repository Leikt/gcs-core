echo "Do thinks for {{ vm }}"
{% commands %}
script001.sh
command101.sh s1 s2 s3 -a
command100.sh {{ vm }}
{% endcommands %}