.PHONY: clean run checksum

# Удаление файлов *.enc, *.dec, "images(1).jpeg" и "images(2).jpeg"
clean:
	rm -f *.enc *.dec "images(1).jpeg" "images(2).jpeg"

# Запуск программы с длиной ключа, передается аргумент KEYLENGTH
run: clean
	python3 rsa.py -k $(KEYLENGTH)
	make checksum

# Вычисление MD5 хэшей для всех JPEG файлов
checksum:
	md5sum *.jpeg
