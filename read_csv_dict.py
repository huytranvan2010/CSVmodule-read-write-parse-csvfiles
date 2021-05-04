import csv

with open("names.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # for line in csv_reader:
    #     print(line)

    """
        Nhận thấy khi đọc bằng DictReader() không còn đọc the field names nữa, các line sẽ trả về dạng dictionary
        với keys là tên các trường, values là các giá trị tương ứng các trường tại dòng đó.
        Đọc theo kiểu này mình sẽ biết ngay giá trị là thuộc feature nào ko cần phải vào lại file .csv để xem lại
    """
        # # hoặc truy cập luôn các trường
        # print(line["email"])

    """
        Khi đọc file .csv bằng DictReader rồi lấy data từ đó ghi vào một file mới ta phải cung cấp field names cho 
        file mới do đọc theo DictReader nó không trả về hàng đầu tiên
    """
    with open("write_dict.csv", "w") as new_file:
        fields = ['first_name', 'last_name', 'email']
        csv_writer = csv.DictWriter(new_file, fieldnames=fields, delimiter='\t')

        csv_writer.writeheader()    # cho cái fieldnames làm header

        for line in csv_reader:
            csv_writer.writerow(line)

