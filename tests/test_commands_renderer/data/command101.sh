{% if do_a -%}
echo "Do A"
{%- endif %}
{% for x in services -%}
echo "{{ x }}"
{% endfor %}