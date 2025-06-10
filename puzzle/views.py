import random
import math
from django.shortcuts import render
from .forms import PuzzleForm

def calculate_view(request):
    result = {}
    if request.method == 'POST':
        form = PuzzleForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            text = form.cleaned_data['text']

            if number % 2 == 0:
                number_result = f"The number {number} is even. Its square root is {math.sqrt(number):.2f}."
            else:
                number_result = f"The number {number} is odd. Its cube is {number ** 3}."

            binary = ' '.join(format(ord(c), '08b') for c in text)
            vowels = sum(c.lower() in 'aeiou' for c in text)
            text_result = f"Binary: {binary}\nVowel Count: {vowels}"

            secret = random.randint(1, 100)
            attempts = []
            for i in range(1, 6):
                guess = random.randint(1, 100)
                if guess < secret:
                    attempts.append(f"Attempt {i}: {guess} (Too low!)")
                elif guess > secret:
                    attempts.append(f"Attempt {i}: {guess} (Too high!)")
                else:
                    attempts.append(f"Attempt {i}: {guess} (Correct!)")
                    break
            else:
                attempts.append("Failed to guess the number in 5 tries.")

            treasure_result = f"The secret number is {secret}.<br>" + "<br>".join(attempts)

            result = {
                'number_result': number_result,
                'text_result': text_result,
                'treasure_result': treasure_result
            }
    else:
        form = PuzzleForm()
    
    return render(request, 'puzzle/calculate.html', {'form': form, 'result': result})

