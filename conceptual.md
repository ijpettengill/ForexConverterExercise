### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  JavaScript has diffent classes of variables (const, var, let) and python just has the one.
  The biggest difference is that Java is static while python is dynamic.
  Python has imutable lists called tuples.
  Python has a large library built in that you can import from.


- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  1. dict['c']: 3,
  2. dict.update({'c': 3})

- What is a unit test?
  A unit test works to test a single componenet of a program.

- What is an integration test?
  This test how multiple components work togeather.

- What is the role of web application framework, like Flask?
  Web application frameworks are a "shortcut".
  They have alot of built in logic so that ic can save a lot of code writing.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  URL parameters feel more like “subject of page” scenarios, where URL query parameters feel more like “extra info about page” and are often used when coming from a form.

- How do you collect data from a URL placeholder parameter using Flask?
  You collect data from a URL placeholder param in Flask by storing it as a variable under the same var_name in the app route.

- How do you collect data from the query string using Flask?
  You collect data from the query string in Flask using 'flask.request.args.get()'.

- How do you collect data from the body of the request using Flask?
  by using request.form

- What is a cookie and what kinds of things are they commonly used for?
  It is a small bit of data that is being stored about the user.
  They are commonly used for things like usernames.

- What is the session object in Flask?
  It's like super charged cookies.  It can store multiple bits of imformation acccross multiple pages

- What does Flask's `jsonify()` do?
  It creates a responce that mimics JSON and its application type.
