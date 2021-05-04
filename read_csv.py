import csv

with open('names.csv', 'r') as csv_file:    # mở file kiểu này tí sẽ tự đóng để khỏi quên
    # đọc file
    csv_reader = csv.reader(csv_file)   # không truyền delimiter nó sẽ tự nhận là ",", nếu dùng delimiter khác phải truyền vào

    # # csv_reader lúc này trở thành iterator, chúng ta có thể loop over by rows
    # for line in csv_reader:
    #     print(line)     # mỗi line (row) trả về list, nên nhớ nó lấy luôn cả the firt line of the csv file

    #     # # Hoặc có thể in ra mỗi email thôi
    #     # print(line[2])

    """ Do không muốn đọc names fields (dòng đầu tiên ta có thể sử dụng một số cách như sau: """

    # # Cách 1: sử dụng next(csv_reader) nó sẽ duyệt qua dòng đầu tiên
    # next(csv_reader)
    # for line in csv_reader:
    #     print(line)

    # # Cách 2:
    # first_line = True
    # for line in csv_reader:
    #     if first_line:
    #         first_line = False      # skip the first line
    #     else:
    #         print(line)
    
    """ Lưu sang một file csv mới nhưng sử dụng dash làm delimiter """
    # Mở một file mới
    with open("new_names.csv", "w") as new_file:
        # ghi vào file
        csv_writer = csv.writer(new_file, delimiter="-")    # ko truyển delimiter nó để default ","

        for line in csv_reader:
            csv_writer.writerow(line)   # ghi từng line (row)

        """
            Nhận thấy file mới tạo ra line thứ 2 email cí thêm "" do bản thân email có chứa "-" để tránh nhầm lẫn
            khi đọc nó đã thêm "" vào giá trị trường đó.
            Tương tự với last_name ở line thứ 3
        """
        """
            Nếu delimiter không phải là "," khi đọc file.csv cần thêm delimiter vào để tránh đọc sai cấu trúc
        """
        """
            Còn một cách đọc .csv file theo dictionary. Cách này có vẻ hay hơn cách thông thường phía trên.
            Cùng xem ở file read_csv_dict.py
        """






