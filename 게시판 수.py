total_count = int(input('게시글의 총 갯수를 입력하세요 :'))
one_page_count = int(input('한 페이지에 필요한 게시글 수를 입력하세요 : '))

page = int(total_count/one_page_count)
print(page)


