{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "cd0ff88f",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, request, render_template"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "d72039b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "7f280427",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "aec212b1",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/\", methods = [\"GET\", \"POST\"])\n",
    "def index():\n",
    "    if request.method == \"POST\":\n",
    "        rates = float(request.form.get(\"rates\"))\n",
    "        print(rates)\n",
    "        model1 = joblib.load(\"Regression\")\n",
    "        pred1 = model1.predict([[rates]])\n",
    "        model2 = joblib.load(\"DecisionTree\")\n",
    "        pred2 = model2.predict([[rates]])\n",
    "        return(render_template(\"index.html\", result1=pred1, result2=pred2))\n",
    "    else:\n",
    "        return(render_template(\"index.html\", result1=\"Waiting\", result2=\"Waiting\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "281626ff",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "[2022-07-07 10:50:15,643] ERROR in app: Exception on / [GET]\n",
      "Traceback (most recent call last):\n",
      "  File \"/opt/anaconda3/lib/python3.9/site-packages/flask/app.py\", line 2447, in wsgi_app\n",
      "    response = self.full_dispatch_request()\n",
      "  File \"/opt/anaconda3/lib/python3.9/site-packages/flask/app.py\", line 1952, in full_dispatch_request\n",
      "    rv = self.handle_user_exception(e)\n",
      "  File \"/opt/anaconda3/lib/python3.9/site-packages/flask/app.py\", line 1821, in handle_user_exception\n",
      "    reraise(exc_type, exc_value, tb)\n",
      "  File \"/opt/anaconda3/lib/python3.9/site-packages/flask/_compat.py\", line 39, in reraise\n",
      "    raise value\n",
      "  File \"/opt/anaconda3/lib/python3.9/site-packages/flask/app.py\", line 1950, in full_dispatch_request\n",
      "    rv = self.dispatch_request()\n",
      "  File \"/opt/anaconda3/lib/python3.9/site-packages/flask/app.py\", line 1936, in dispatch_request\n",
      "    return self.view_functions[rule.endpoint](**req.view_args)\n",
      "  File \"/var/folders/y1/jqxczpsx5b16319pk3pr6xr80000gn/T/ipykernel_69416/3108415135.py\", line 12, in index\n",
      "    return(render_template(\"index.html\", result1=\"Waiting\", result2=\"Waiting\"))\n",
      "  File \"/opt/anaconda3/lib/python3.9/site-packages/flask/templating.py\", line 138, in render_template\n",
      "    ctx.app.jinja_env.get_or_select_template(template_name_or_list),\n",
      "  File \"/opt/anaconda3/lib/python3.9/site-packages/jinja2/environment.py\", line 930, in get_or_select_template\n",
      "    return self.get_template(template_name_or_list, parent, globals)\n",
      "  File \"/opt/anaconda3/lib/python3.9/site-packages/jinja2/environment.py\", line 883, in get_template\n",
      "    return self._load_template(name, self.make_globals(globals))\n",
      "  File \"/opt/anaconda3/lib/python3.9/site-packages/jinja2/environment.py\", line 857, in _load_template\n",
      "    template = self.loader.load(self, name, globals)\n",
      "  File \"/opt/anaconda3/lib/python3.9/site-packages/jinja2/loaders.py\", line 115, in load\n",
      "    source, filename, uptodate = self.get_source(environment, name)\n",
      "  File \"/opt/anaconda3/lib/python3.9/site-packages/flask/templating.py\", line 60, in get_source\n",
      "    return self._get_source_fast(environment, template)\n",
      "  File \"/opt/anaconda3/lib/python3.9/site-packages/flask/templating.py\", line 89, in _get_source_fast\n",
      "    raise TemplateNotFound(template)\n",
      "jinja2.exceptions.TemplateNotFound: index.html\n",
      "127.0.0.1 - - [07/Jul/2022 10:50:15] \"GET / HTTP/1.1\" 500 -\n"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "656507d5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
