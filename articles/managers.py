from articles.models import Article
from users.models import Profile
from d3.logger import log


class ArticleManager:
    def get(self, uuid: str) -> Article:
        try:
            article = Article.objects.get(uuid=uuid)
        except Article.DoesNotExist:
            log(log.ERROR, "Failed to get article [%s]: article does not exist", uuid)
            return None

        log(log.INFO, "Got article [%s]", uuid)
        return article

    def get_all(self) -> list[Article]:
        articles = Article.objects.all()
        log(log.INFO, "Got [%d] articles", len(articles))
        return articles

    def post(self, data) -> tuple[Article, str]:
        author_id = data["author_id"]
        try:
            author = Profile.objects.get(id=author_id)
        except Profile.DoesNotExist:
            log(
                log.ERROR,
                "Failed to create article: author [%d] does not exist",
                author_id,
            )
            return None, "Author does not exist"

        try:
            article = Article.objects.create(
                author=author,
                title=data["title"],
                content=data["content"],
            )
        except Exception as e:
            log(log.ERROR, "Failed to create article: %s", str(e))
            return None, "Failed to create article"

        log(log.INFO, "Created article [%s]", article.uuid)
        return article, None

    def put(self, article: Article, data) -> tuple[bool, str]:
        try:
            assert article
            # article.title = data.get("title", article.title)
            # article.content = data.get("content", article.content)
            for attr, value in data.items():
                if attr == "users_liked":
                    article.users_liked.add(value)
                    article.save()
                else:
                    setattr(article, attr, value)
            article.save()
        except Exception as e:
            log(log.ERROR, "Failed to update article [%s]: %s", article.uuid, str(e))
            return False, "Failed to update article"

        log(log.INFO, "Updated article [%s]", article.uuid)
        return True, None
