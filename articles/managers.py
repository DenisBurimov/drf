from articles.models import Article
from users.models import Profile
from d3.logger import log


def create_new_article(data) -> tuple[Article, str]:
    author_id = data["author_id"]
    try:
        author = Profile.objects.get(id=author_id)
    except Profile.DoesNotExist:
        log(
            log.ERROR, "Failed to create article: author [%d] does not exist", author_id
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
