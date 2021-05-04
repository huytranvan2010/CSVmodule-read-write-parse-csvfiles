# CSVmodule-read-write-parse-csvfiles
Csv file thường được tổ chức theo các hàng với hàng đầu tên là tên các cột, các trường giá trị ngăn cách nhau bằng dấu "," (hay được sử dụng, còn có một số delimiter khác).

Hiện tại chúng ta có sắn file `names.csv` với dòng đầu tiên là tên các cột `first_name`, `last_name`, `email`. Các dòng bên dưới gọi là các bản ghi `record`.

Để đọc `.csv` file ta tạo một file `read_csv.py`. Sử dụng method `csv.reader()` để đọc file. Do trả về iterator nên ta có thể duyệt qua từng hàng.

Muốn ghi file ta sẽ sử dụng method `csv.writer()`, có thể ghi theo từng dòng hoặc nhiều dòng.

Ngoài cách đọc fle csv thông thường phía trên còn có cách khác đọc file csv theo kiểu dictionary. 
Nhận thấy khi đọc bằng DictReader() không còn đọc the field names nữa, các line sẽ trả về dạng dictionary với keys là tên các trường, values là các giá trị tương ứng các trường tại dòng đó. Đọc theo kiểu này mình sẽ biết ngay giá trị là thuộc feature nào ko cần phải vào lại file .csv để xem lại.

Khi đọc file .csv bằng DictReader rồi lấy data từ đó ghi vào một file mới ta phải cung cấp field names cho file mới do đọc theo DictReader nó không trả về hàng đầu tiên.

# Tài liệu tham khảo
https://www.geeksforgeeks.org/working-csv-files-python/
https://www.youtube.com/watch?v=q5uM4VKywbA
