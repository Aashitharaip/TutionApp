# References


1. [Django User Login](https://realpython.com/django-user-management/)

## How to do login page

* create `templates/registration/login.html`
* add `{{ form }}` variable in `login.html`
* you can change `{{ form }}` by changing it to `form.as_p` or `form.as_table` etc
* add `path('accounts/', include('django.contrib.auth.urls'))` in `project.urls`
* logout using
```html
<form action="{% url 'logout' %}" method="post">
    {% csrf_token %}
    <button class="btn btn-dark">Logout</button>
</form>
```

* to redirect user after logout use settings.py
`LOGOUT_REDIRECT_URL = '/'`

* to redirect unauthorized persons use `@login_required` decorator
* `from django.contrib.auth.decorators import login_required`


```py

@login_required
def dashboard(request):
    return render(request, "dashboard.html")

```


