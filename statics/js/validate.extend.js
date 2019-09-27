jQuery.extend(jQuery.validator.messages, {
    required: "* Campo obrigatório.",
    remote: "Please fix this field.",
    email: "Insira um e-mail válido.",
    url: "Insira uma URL válida.",
    date: "Insira uma data válida.",
    dateISO: "Please enter a valid date (ISO).",
    number: "Insira um número válido.",
    digits: "Please enter only digits.",
    creditcard: "Please enter a valid credit card number.",
    equalTo: "Please enter the same value again.",
    accept: "Please enter a value with a valid extension.",
    maxlength: jQuery.validator.format("Please enter no more than {0} characters."),
    minlength: jQuery.validator.format("Please enter at least {0} characters."),
    rangelength: jQuery.validator.format("Please enter a value between {0} and {1} characters long."),
    range: jQuery.validator.format("Insira um valor entre {0} e {1}."),
    max: jQuery.validator.format("Insira um valor menor ou igual a {0}."),
    min: jQuery.validator.format("Insira um valor maior ou igual a {0}.")
});
