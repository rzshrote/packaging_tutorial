{{ fullname | escape | underline }}

.. rubric:: Description

.. automodule:: {{ fullname }}

.. currentmodule:: {{ fullname }}

{% block attributes %}
{% if attributes %}
   .. rubric:: Attributes
   .. autosummary::
      :toctree:
      {% for item in attributes %}
      {{ item }}
      {%- endfor %}
{% endif %}
{% endblock %}


{% block classes %}
{% if classes %}
.. rubric:: Classes
.. autosummary::
    :toctree:
    {% for item in classes %}
    {{ item }}
    {% endfor %}
{% endif %}
{% endblock %}


{% block functions %}
{% if functions %}
.. rubric:: Functions
.. autosummary::
    :toctree:
    {% for item in functions %}
    {{ item }}
    {% endfor %}
{% endif %}
{% endblock %}


{% block modules %}
{% if modules %}
.. rubric:: Modules
.. autosummary::
    :toctree:
    {% for item in modules %}
    {{ item }}
    {% endfor %}
{% endif %}
{% endblock %}
