# Dars rejasi

1. Django va Django Rest Framework larni o'rnatib oldik
    
2. O'zimizga kerak bo'lgan app larni ochib oldik
3. Modellar yozdik
4. Send email messages ni ko'rdik
5. User uchun Register API ishlab chiqdik
6. User uchun Login va VerifyEmail API ishlab chiqdik
7. Category uchun  CRUD API ishlab chiqdik
8. Article uchun CRUD API ishlab chiqdik


# Class va Method lar

### GenericAPIView
- ListAPIView
- CreateAPIView
- RetrieveAPIView
- UpdateAPIView
- DestroyAPIView - bu faqat bazadagi ma'lumotni o'chiruvchi class, DELETE method ni qabul qiladi
- RetrieveUpdateDestroyAPIView - 3 ta class ni birlashtirgan class

### Useful methods

- get_queryset() - bu methodni override qilish orqali, queryset ni filter qilish mumkin
- select_related() - bu methodni override qilish orqali, queryset ni join qilish mumkin, foreign key bo'lgan fieldlarni bitta connection da olish uchun ishlatiladi
- prefetch_related() - bu methodni override qilish orqali, queryset ni join qilish mumkin, many to many fieldlarni bitta connection da olish uchun ishlatiladi


### Keyingi darsda

## Studentlar uchun
- Genre va Award modellar uchun API ko'tarish

## O'qituvchi uchun
- API ni test lashni ko'ramiz
- Qolgan modellar uchun API ko'tarishni davom etamiz!


#### Meme time 🕜:
- Backendchi bu - Frontni, Backni, Devopsdan oz-moz bilishi kerak va Tester lik qobiliyati ham bo'lishi kerak.

