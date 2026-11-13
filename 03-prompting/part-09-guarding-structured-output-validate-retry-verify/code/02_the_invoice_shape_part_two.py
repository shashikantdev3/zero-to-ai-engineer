"""Zero to AI Engineer · Prompting · Part 9 of 10
Slide: The invoice shape, part two
Run: python 02_the_invoice_shape_part_two.py
"""
# Note: this is a fragment from the slide. It uses names that are set up elsewhere (for example a model client),
# so on its own it stops with NameError.
class Invoice(BaseModel):
    invoice_no: str
    currency: Literal["INR", "USD", "EUR"]
    lines: list[Line] = Field(min_length=1)
    tax: Decimal = Field(ge=0)
    total: Decimal = Field(gt=0)
    @field_validator("invoice_no")
    @classmethod
    def strip_no(cls, v: str) -> str:
        return v.strip().upper()
# raw_text is the model's reply
inv = Invoice.model_validate_json(raw_text)
