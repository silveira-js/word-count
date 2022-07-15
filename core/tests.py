import string

from django.test import TestCase
from .forms import TextForm
from.views import word_counter


class FormTests(TestCase):

    def test_form_valid(self):
        form_data = {'text': 'something is great'}
        form = TextForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_validation_for_blank_items(self):
        form = TextForm(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['text'],
            ["Your text must not be empty"]
        )

    def test_form_item_input_has_placeholder_and_css_classes(self):
        form = TextForm()
        self.assertIn('placeholder="Enter your text here..."', form.as_p())
        self.assertIn('class="form-class"', form.as_p())


class HomePageTest(TestCase):

    def test_home_page_renders_template(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/index.html')

    def test_home_page_uses_item_form(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['form'], TextForm)

    def test_add_text_form_view(self):
        response = self.client.post('/', {'text': 'some text'})
        self.assertEqual(response.status_code, 200)

    def test_add_text_error(self):
        response = self.client.post('/', data={'text': ''})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Your text must not be empty', html=True)


class WordCounter(TestCase):

    def test_word_counter_punctuation(self):
        text = "Text. With. Punctuation!"
        text2 = string.punctuation
        self.assertEqual(word_counter(text), 3)
        self.assertEqual(word_counter(text2), 0)

    def test_word_counter_number(self):
        text = "This text have      number 3 2 1 and 5"
        self.assertEqual(word_counter(text), 5)

    def test_word_counter_with_text_without_spaces(self):
        text = "Text.With.Punctuation!23 45 65"
        self.assertEqual(word_counter(text), 3)


    
    
