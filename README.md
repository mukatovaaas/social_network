# social_network
IITU Final Project [ NSA4: Networking and Security (SDP9) (c.w.) (Алшынов Ш.К.) ]

Models:
  Follower  (id, follower, following)
  Post      (id, user, content, created_at)
  Like      (id, user, post)
  Comment   (id, user, post, content)
  Message   (id, sender, recipient, message, created_at)

Endpoints:
  for authorization and authentication djoser package is used
  get   'followers/'        lists followers
  get   'following/'        lists following users
  get   'posts/<int:pk>'    lists user posts
  post  'like/'             like user post
  get   'comments/<int:pk>' list comments of post
  get   'posts/'            list request.user posts
  post  'post/'             create a post  
  post  'follow/'           follow user
  post  'unfollow/'         unfollow user
  get/post  'chat/'         list messages/send message to user
  get   'chat/<int:user>'   list messages with request.user and user
  get   'search/',          search user by username
