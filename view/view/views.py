# 학생의 번호, 국어, 영어, 수학 점수를 전달받은 뒤
# 총점과 평균을 화면에 출력한다.
import random

from django.shortcuts import render, redirect
from django.views import View


# form태그는 get방식을 사용한다.
# 출력 화면에서 다시 입력화면으로 돌아갈 수 있게 한다.

# 입력: task/student/register.html
# 출력: task/student/result.html

class StudentRegisterFormView(View):
    def get(self, request):
        return render(request, 'task/student/register.html')


class StudentRegisterView(View):
    def get(self, request):
        data = request.GET
        data = {
            'number': int(data['number']),
            'korean': int(data['korean']),
            'english': int(data['english']),
            'math': int(data['math'])
        }
        total = data['korean'] + data['english'] + data['math']
        average = round(total / 3, 2)

        return redirect(f'/student/result?number={data["number"]}&total={total}&average={average}')


class StudentResultView(View):
    def get(self, request):
        data = request.GET
        context = {
            'number': data['number'],
            'total': data['total'],
            'average': data['average']
        }
        return render(request, 'task/student/result.html', context)

# 회원의 이름과 나이를 전달받는다.
# 전달받은 이름과 나이를 아래와 같은 형식으로 변경시킨다.
# "홍길동님은 20살!"
# 결과 화면으로 이동한다.

# 이름과 나이 작성: task/member/register.html
# 결과 출력: task/member/result.html

class MemberRegisterFormView(View):
    def get(self, request):
        return render(request, 'task/member/register.html')


class MemberRegisterView(View):
    def get(self, request):
        data = request.GET
        data = {
            'name': data['name'],
            'age': data['age']
        }

        return redirect(f'/member/result?name={data["name"]}&age={data["age"]}')


class MemberResultView(View):
    def get(self, request):
        data = request.GET
        context = {
            'name': data['name'],
            'age': data['age']
        }

        return render(request, 'task/member/result.html', context)

# 회원의 이름과 나이를 전달 받은 후,
# 20살 미만이면 "지원님은 미성년자 입니다"
# 20살 이상이면 "지원님은 성인이시군요!"
# 결과 화면에 문구 출력하기

# 작성: task/user/register.html
# 출력: task/user/result.html

class UserRegisterFormView(View):
    def get(self, request):
        return render(request, 'task/user/register.html')


class UserRegisterView(View):
    def get(self, request):
        data = request.GET
        name = data['name']
        age = int(data['age'])
        result = ""
        if age >= 20:
            result = f"{data.get('name')}님은 성인이시군요!"
        else:
            result = f"{data.get('name')}님은 미성년자입니다."

        return redirect(f'/user/result?result={result}')


class UserResultView(View):
    def get(self, request):
        result = request.GET['result']
        return render(request, 'task/user/result.html', {'result': result})

# 1~10사이의 숫자를 입력받아(input[type=number])
# 뷰에서 1~10사이의 랜덤한 숫자(random.randint())를 생성한 후
# 일치할 경우 "축하합니다! 정답입니다!"를 화면으로,
# 불일치할 경우 차이(절댓값)를 "아쉽네요... 정답과 [차이]만큼 차이가 나요!" 출력하기
# 작성: task/number/input.html
# 출력: task/number/result.html

class NumberInputFormView(View):
    def get(self, request):
        return render(request, 'task/number/input.html')


class NumberInputView(View):
    def get(self, request):
        number = int(request.GET['number'])
        answer = random.randint(0, 10)
        result = ""
        if number == answer:
            result = "축하합니다! 정답입니다!"
        else:
            result = f"아쉽네요... 정답과 {abs(number-answer)}만큼 차이가 나요!"

        return redirect(f'/number/result?result={result}')


class NumberResultView(View):
    def get(self, request):
        result = request.GET['result']
        return render(request, 'task/number/result.html', {'result': result})


# 사용자에게 영문 텍스트를 입력 받은 후
# 대문자를 소문자로 소문자를 대문자로 출력하기
# 작성: task/text/register.html
# 출력: task/text/result.html

class TextRegisterFormView(View):
    def get(self, request):
        return render(request, 'task/text/register.html')


class TextRegisterView(View):
    def get(self, request):
        text = request.GET['text']
        result = ""
        for s in text:
            if s.isalpha():
                if 65 <= ord(s) <= 90:
                    result += s.lower()
                else:
                    result += s.upper()
            else:
                result += s
        return redirect(f'/text/result?result={result}')


class TextResultView(View):
    def get(self, request):
        result = request.GET['result']
        return render(request, 'task/text/result.html', {'result': result})


# 회원의 이름 /제목/ 내용을 받고
# (이름)회원님이 (제목)이라는 주제의 이벤트를 만들었어요!
# (내용)하실분~~
# 이라는 내용 출력하기
# 작성: task/event/register.html
# 출력: task/event/result.html (편집됨)

class EventRegisterFormView(View):
    def get(self, request):
        return render(request, 'task/event/register.html')


class EventRegisterView(View):
    def get(self, request):
        data = request.GET
        result = f"{data['name']}회원님이 {data['title']}이라는 주제의 이벤트를 만들었어요!\n{data['content']}하실분~~"
        return redirect(f'/event/result?result={result}')


class EventResultView(View):
    def get(self, request):
        result = request.GET['result']
        return render(request, 'task/event/result.html', {'result': result})


# 사용자에게 숫자를 입력 받기
# 입력 받은 숫자는 몇 자리 숫자인지 출력하기
# 출력 예시: [입력한 숫자]는 N의 자리 입니다~!

# 작성: task/num/register.html
# 출력: task/num/result.html

class NumRegisterFormView(View):
    def get(self, request):
        return render(request, 'task/num/register.html')


class NumRegisterView(View):
    def get(self, request):
        number = request.GET['number']
        number_len = len(number)
        number = int(number)
        result = f"{number}는 {number_len}의 자리 입니다~!"
        return redirect(f'/num/result?result={result}')


class NumResultView(View):
    def get(self, request):
        result = request.GET['result']
        return render(request, 'task/num/result.html', {'result': result})

# 상품 정보
# 번호, 상품명, 가격, 재고
# 상품 1개 정보를 REST 방식으로 설계한 뒤
# 화면에 출력하기
# 예시)
# product/1
# task/product/product-list.html







