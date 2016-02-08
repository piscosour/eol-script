## This parrot is no more. It has ceased to be. It's expired and gone to meet its maker. This is a late parrot. It's a stiff. Bereft of life, it rests in peace. If you hadn't nailed it to the perch, it would be pushing up the daisies. It's rung down the curtain and joined the choir invisible. This is an ex-parrot.
 
if eduardo.life == False and eduardo.zombie == False:
	## Handle email accounts
	for account in eduardo.email:
		for message in account:
			if message.has_tag("bury"):
				message.add_to_timelock(3650)
			elif message.has_tag("wipe"):
				message.delete()
			elif message.has_tag("share"):
				message.forward_to(message.target)
			else:
				eduardo.archive = eduardo.archive + [message]
 
	## Handle Facebook
	for post in eduardo.facebook.posts:
		eduardo.archive = eduardo.archive + [post]
	eduardo.facebook.post_message("Well this was fun. We should do this again sometime.")
	for message in eduardo.facebook.messages:
		message.delete()
 
	## Handle Twitter
	eduardo.twitter.post_message("Well this was fun. We should do this again sometime.")
	for tweet in eduardo.twitter.messages:
		eduardo.archive = eduardo.archive + [tweet]
	eduardo.twitter.set_password(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20)))
 
	## Delete any other social media accounts
	for account in eduardo.other_social_media:
		account.shutdown()
 
	## Delegate project access/control to other people
	for element in eduardo.projects:
		element.delegate(assigned_caretaker)
 
	## Set up an online archive for relevant stuff
	eduardo.archive.sort(key=lambda x: x.timestamp)
	for element in eduardo.archive:
		element.publish(online_tombstone)
 
elif eduardo.life == False and eduardo.zombie == True:
	eduardo.kill("shotgun", "head")