## Script (Python) "ecl_register"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=group=''
##title=
##

I18N_DOMAIN = 'eduComponents'

REQUEST  = container.REQUEST
RESPONSE = REQUEST.RESPONSE
# print REQUEST
# return printed

# user_id = REQUEST.get('user_id', None)
# user_id = member.getId()

user_id = str(REQUEST.get('AUTHENTICATED_USER', None))
member  = context.portal_membership.getMemberById(str(user_id))
groups  = member.getGroups()
action  = ''
status  = 'failure'
msg     = 'Enrollment error'

if not context.isParticipant(user_id):
    action = 'add'
    ret = context.addParticipant(user_id)
else:
    action = 'remove'
    ret = context.removeParticipant(user_id)

if ret:
    status = 'success'
else:
    status = 'failure'

if action == 'add' and status == 'success':
    msg = context.translate(
        msgid   = 'enrollment_sucessful',
        domain  = I18N_DOMAIN,
        default = 'You have been successfully enrolled.')
elif action == 'add' and status == 'failure':
    msg = context.translate(
        msgid   = 'enrollment_failed',
        domain  = I18N_DOMAIN,
        default = 'Enrollment failed, please contact the instructor.')
elif action == 'remove' and status == 'success':
    msg = context.translate(
        msgid   = 'cancellation_successful',
        domain  = I18N_DOMAIN,
        default = 'You are no longer enrolled.')
elif action == 'remove' and status == 'failure':
    msg = context.translate(
        msgid   = 'cancellation_failed',
        domain  = I18N_DOMAIN,
        default = 'Cancellation of enrollment failed, please contact the instructor.')

#return state.set(status = status, portal_status_message = msg)
RESPONSE.redirect('%s?portal_status_message=%s' % 
            (context.absolute_url(), msg,))
