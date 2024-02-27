def konversi_nilai(nilai):
    
    if nilai >= 80:
        return "A"
    elif nilai >= 70:
        return "B"
    return ''

student_score = 80
if __name__ == '__main__':
    print(konversi_nilai(80))