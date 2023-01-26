# 0. from NewsPortal.models import *
# 1. User.objects.create_user('username_1')
# 1. User.objects.create_user('username_2')
# 2. author_1 = Author.objects.create(user_id=1)
# 2. author_1.save()
# 2. author_2 = Author.objects.create(user_id=2)
# 2. author_2.save()
# 3. category_1 = Category.objects.create(name='Category_1')
# 3. category_1.save()
# 3. category_2 = Category.objects.create(name='Category_2')
# 3. category_2.save()
# 3. category_3 = Category.objects.create(name='Category_3')
# 3. category_3.save()
# 3. category_4 = Category.objects.create(name='Category_4')
# 3. category_4.save()
# 4. post_1 = Post.objects.create(author=Author(id=1), headline='headline_1', text='text_1')
# 4. post_1.save()
# 4. post_2 = Post.objects.create(author=Author(id=2), headline='headline_2', text='text_2')
# 4. post_2.save()
# 4. post_3 = Post.objects.create(author=Author(id=2), post_or_news='news', headline='headline_3', text='text_3')
# 4. post_3.save()
# 5. post_1.category.add(category_1, category_2)
# 5. post_2.category.add(category_2, category_3)
# 5. post_3.category.add(category_3, category_4)
# 6. comment_1 = Comment.objects.create(post=Post(id=1), user=User(id=2), text='comment_text_1')
# 6. comment_1.save()
# 6. comment_2 = Comment.objects.create(post=Post(id=1), user=User(id=1), text='comment_text_2')
# 6. comment_2.save()
# 6. comment_3 = Comment.objects.create(post=Post(id=2), user=User(id=1), text='comment_text_3')
# 6. comment_3.save()
# 6. comment_4 = Comment.objects.create(post=Post(id=3), user=User(id=2), text='comment_text_4')
# 6. comment_4.save()
# 7. post_1.like()
# 7. post_1.save()
# 7. post_1.like()
# 7. post_1.save()
# 7. post_2.dislike()
# 7. post_2.save()
# 7. post_3.like()
# 7. post_3.save()
# 7. comment_1.like()
# 7. comment_1.save()
# 7. comment_2.dislike()
# 7. comment_2.save()
# 7. comment_3.like()
# 7. comment_3.save()
# 7. comment_4.dislike()
# 7. comment_4.save()
# 8. author_1.update_rating()
# 8. author_2.update_rating()
# 9. best_author = Author.objects.all().order_by('-user_rating')[0]
# 9. best_author.user_rating
# 9. best_author.user.username
# 10. best_post = Post.objects.all().order_by('-rating')[0]
# 10. best_post.pub_date
# 10. best_post.author.user.username
# 10. best_post.rating
# 10. best_post.headline
# 10. best_post.preview()
# 11. best_post_comments = Comment.objects.filter(post=best_post)
# 11. best_post_comments.values('pub_date', 'user', 'rating', 'text')
