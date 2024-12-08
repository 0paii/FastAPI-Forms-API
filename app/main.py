from fastapi import FastAPI, Request
from app.database import get_templates
from app.validation import TYPE_VALIDATORS, template_validation
import uvicorn
from typing import Dict

app = FastAPI()


@app.get("/")
async def homepage():
    """Просмотр всех шаблонов на главной странице"""
    template = get_templates()
    return [str(i) for i in template]


def get_field_types(form_data: dict) -> Dict[str, str]:
    """
    Определение типа полей формы.

    :param form_data: словарь с данными формы
    :return: словарь с типами полей
    """
    result = {}
    for key, value in form_data.items():
        for field_type, validator in TYPE_VALIDATORS.items():
            if validator(value):
                result.update({key: field_type})
                break
    return result


@app.post("/get_form")
async def get_form(request: Request):
    templates = get_templates()
    form_data = await request.form()
    form_dict = dict(form_data)

    valid_templates = []

    for template in templates:
        if (n := template_validation(template, form_dict)) > 0:
            valid_templates.append({"template_name": template["name"], "fields": n})
    if not valid_templates:
        return get_field_types(form_dict)
    elif len(valid_templates) == 1:
        return valid_templates[0]['template_name']
    else:
        return sorted(valid_templates, key=lambda x: x['fields'], reverse=True)[0]['template_name']


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
