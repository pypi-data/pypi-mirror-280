import pytest
from src.interface import Schema, Section
from src.args import Parameters
from pathlib import Path
import random
from dataclasses import dataclass


@dataclass(slots=True)
class Markers:
    entity_delimiter: str
    option_delimiter: str
    comment_prefix: str
    continuation_prefix: str


@pytest.fixture
def default_content():
    def shuffle_content(content):
        if isinstance(content, dict):
            for k, v in content.items():
                content[k] = shuffle_content(v)
        elif isinstance(content, list):
            random.shuffle(content)
            for i in content:
                shuffle_content(i)
        return content

    content = [
        "comment_1",
        "comment_2",
        "comment_3",
        {
            "sec-1": [
                "sec-1_comment-1",
                "sec-1_comment-2",
                "sec-1_comment-3",
                {"sec-1_opt-1": "sec-1_opt-1_val-1"},
                {"sec-1_opt-2": "sec-1_opt-2_val-1"},
            ]
        },
        {
            "sec-2": [
                {"sec-2_opt-1": "sec-2_opt-1_val-1"},
                {"sec-2_opt-2": "sec-2_opt-2_val-1"},
            ]
        },
        {
            "sec-1": [
                "sec-1_comment-4",
                {"sec-1_opt-3": "sec-1_opt-3_val-1"},
                {"sec-1_opt-2": ("sec-1_opt-2_val-21", "sec-1_opt-2_val-22")},
            ]
        },
        {
            "sec-2": [
                "sec-2_comment-1",
                {"sec-2_opt-3": ("sec-2_opt-3_val-11", "sec-2_opt-3_val-12")},
                {"sec-2_undefopt": "sec-1_undefopt_val-1"},
            ]
        },
        {
            "undefsec": [
                "undefsec_comment-1",
                {"undefsec_opt-1": "undefsec_opt-1_val-1"},
            ]
        },
    ]
    shuffle_content(content)
    return [
        {"undefopt-1": "undefopt-1_value-1"},
        {"undefopt-2": "undefopt-2_value-1"},
        *content,
    ]

@pytest.fixture
def content_as_str(default_content, markers):
    def entities_to_str(entities) -> str:
        out = ""
        for entity in entities:
            if isinstance(entity, dict):
                for k, v in entity.items():
                    if isinstance(v, list):
                        out += f"[{k}]{markers.entity_delimiter*2}"
                        out += entities_to_str(v)
                    else:
                        value = (
                            v
                            if isinstance(v, str)
                            else markers.continuation_prefix.join(v)
                        )
                        out += f"{k} {markers.option_delimiter} {value}"
                    out += markers.entity_delimiter * 2
            else:
                out += f"{markers.comment_prefix} {entity}{markers.entity_delimiter}"
        return out

    return entities_to_str(default_content())


@pytest.fixture(scope="session")
def default_file(tmp_path_factory, content_as_str):
    fn = tmp_path_factory.mktemp("inis") / "test.ini"
    fn.write_text(content_as_str)
    return fn

@pytest.fixture
def markers():
    random_unicode = lambda: chr(random.randint(0, 1114111))
    return Markers(
        entity_delimiter=random_unicode(),
        option_delimiter=random_unicode(),
        comment_prefix=random_unicode(),
        continuation_prefix=random_unicode(),
    )

@pytest.fixture
def schema():
    class INI(Schema):
        class Sec_1:
            _name = "sec-1"
            sec_1_opt_1 = "sec-1_opt-1"
            sec_1_opt_2 = "sec-1_opt-2"
            sec_1_opt_3 = "sec-1_opt-3"

        class Sec_2:
            _name = "sec-2"
            sec_2_opt_1 = "sec-2_opt-1"
            sec_2_opt_2 = "sec-2_opt-2"
            sec_2_opt_3 = "sec-2_opt-3"
    
    return INI


def test_continuation(schema,markers,cont):
    
    
@pytest.fixture
def 

    ini = schema(
        parameters=Parameters(
            multiline_allowed=cont,
            multiline_ignore=("option",),
            multiline_prefix=markers.continuation_prefix * random.randint(1, 1000),
            comment_prefixes=markers.comment_prefix,
            entity_delimiter=markers.entity_delimiter,
            option_delimiters=markers.option_delimiter,
        )
    )