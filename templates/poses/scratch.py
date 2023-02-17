{% if is_paginated %}
  <div class="pagination">
    <span class="step-links">
        {% if page.has_previous %}
            <a href="?page=1">&laquo; first</a>
            <a href="?page={{ page.previous_page_number }}">previous</a>
        {% endif %}

        <span class="current-page">
            Page {{ page.number }} of {{ page.paginator.num_pages }}.
        </span>

        {% if page.has_next %}
            <a href="?page={{ page.next_page_number }}">next</a>
            <a href="?page={{ page.paginator.num_pages }}">last &raquo;</a>
        {% endif %}
    </span>
  </div>
{% endif %}

<table>
  <thead>
    <tr>
      <th>#</th>
      <th>Column1</th>
      <th>Column2</th>
      <th>Column3</th>
    </tr>
  </thead>
  <tbody>
    {% for item in items %}
      <tr>
        <td>{{ forloop.counter0|add:((page.number-1)*page.paginator.per_page)|add:1 }}</td>
        <td>{{ item.column1 }}</td>
        <td>{{ item.column2 }}</td>
        <td>{{ item.column3 }}</td>
      </tr>
    {% endfor %}
  </tbody>
</table>
