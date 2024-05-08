from articles.models import Article, Comment
from users.models import Profile
from d3.logger import log


class CommentManager:
    def post_comment(self, article: Article, data) -> tuple[Comment, str]:
        """
        Wrong data:
        {'text': 'Test Comment', 'user_id': 1}
        """
        author_id = data["author_id"]

        try:
            author = Profile.objects.get(id=author_id)
        except Profile.DoesNotExist:
            log(
                log.ERROR,
                "Failed to create comment: author [%d] does not exist",
                author_id,
            )
            return None, "Author does not exist"

        try:
            comment = Comment.objects.create(
                text=data["text"],
                article=article,
                author=author,
            )
        except Exception as e:
            log(log.ERROR, "Failed to create comment: %s", str(e))
            return None, "Failed to create comment"

        log(log.INFO, "Created comment [%s]", comment.uuid)
        return comment, None
