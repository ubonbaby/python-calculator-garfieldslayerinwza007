class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        if b < 0:
            b_positive = 0 - b
            for i in range(b_positive): 
                result = self.add(result, a)
            result = 0 - result
        else:
            for i in range(b): 
                result = self.add(result, a)
        return result

    def divide(self, a, b):
        if b == 0:
            # ป้องกันการหารด้วยศูนย์
            return 0 

        result = 0
        a_is_neg = a < 0
        b_is_neg = b < 0
        
        a_pos = a if not a_is_neg else (0 - a)
        b_pos = b if not b_is_neg else (0 - b)

        # แก้ไข Bug 'while a > b' เป็น 'while a_pos >= b_pos'
        while a_pos >= b_pos:
            # self.subtract ที่แก้ไขแล้ว
            a_pos = self.subtract(a_pos, b_pos) 
            result = self.add(result, 1)

        # หากเครื่องหมายต่างกัน ผลลัพธ์ต้องเป็นลบ
        if a_is_neg != b_is_neg:
            result = 0 - result
            
        return result

    def modulo(self, a, b):
        if b == 0:
            return 0 
            
        # 1. หา quotient (a // b)
        quotient = self.divide(a, b)
        
        # 2. หา (b * quotient)
        b_times_quotient = self.multiply(b, quotient)
        
        # 3. หา a - (b * quotient)
        remainder = self.subtract(a, b_times_quotient)
        
        return remainder