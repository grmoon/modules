const environment = process.env.NODE_ENV;
const isProduction = environment == 'production';
let rules;

if (!isProduction) {
    rules = {
        'no-console': 'off',
        'no-debugger': 'off'
    };
}
else {
    rules = {};
}

module.exports = {
    extends: [
        'eslint:recommended',
        'plugin:vue/recommended'
    ],
    rules
}