"""Github STG

Revision ID: d459997cd681
Revises: 1100c470c547
Create Date: 2024-05-09 12:20:57.740402

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'd459997cd681'
down_revision = '1100c470c547'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table_schema("STG_GITHUB")
    op.create_table(
        'org_info',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('login', sa.String(), nullable=True),
        sa.Column('node_id', sa.String(), nullable=True),
        sa.Column('url', sa.String(), nullable=True),
        sa.Column('repos_url', sa.String(), nullable=True),
        sa.Column('events_url', sa.String(), nullable=True),
        sa.Column('hooks_url', sa.String(), nullable=True),
        sa.Column('issues_url', sa.String(), nullable=True),
        sa.Column('members_url', sa.String(), nullable=True),
        sa.Column('public_members_url', sa.String(), nullable=True),
        sa.Column('avatar_url', sa.String(), nullable=True),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('company', sa.String(), nullable=True),
        sa.Column('blog', sa.String(), nullable=True),
        sa.Column('location', sa.String(), nullable=True),
        sa.Column('email', sa.String(), nullable=True),
        sa.Column('twitter_username', sa.String(), nullable=True),
        sa.Column('is_verified', sa.String(), nullable=True),
        sa.Column('has_organization_projects', sa.String(), nullable=True),
        sa.Column('has_repository_projects', sa.String(), nullable=True),
        sa.Column('public_repos', sa.String(), nullable=True),
        sa.Column('public_gists', sa.String(), nullable=True),
        sa.Column('followers', sa.String(), nullable=True),
        sa.Column('following', sa.String(), nullable=True),
        sa.Column('html_url', sa.String(), nullable=True),
        sa.Column('created_at', sa.String(), nullable=True),
        sa.Column('updated_at', sa.String(), nullable=True),
        sa.Column('archived_at', sa.String(), nullable=True),
        sa.Column('type', sa.String(), nullable=True),
        sa.Column('total_private_repos', sa.String(), nullable=True),
        sa.Column('owned_private_repos', sa.String(), nullable=True),
        sa.Column('private_gists', sa.String(), nullable=True),
        sa.Column('disk_usage', sa.String(), nullable=True),
        sa.Column('collaborators', sa.String(), nullable=True),
        sa.Column('billing_email', sa.String(), nullable=True),
        sa.Column('default_repository_permission', sa.String(), nullable=True),
        sa.Column('members_can_create_repositories', sa.String(), nullable=True),
        sa.Column('two_factor_requirement_enabled', sa.String(), nullable=True),
        sa.Column('members_allowed_repository_creation_type', sa.String(), nullable=True),
        sa.Column('members_can_create_public_repositories', sa.String(), nullable=True),
        sa.Column('members_can_create_private_repositories', sa.String(), nullable=True),
        sa.Column('members_can_create_internal_repositories', sa.String(), nullable=True),
        sa.Column('members_can_create_pages', sa.String(), nullable=True),
        sa.Column('members_can_fork_private_repositories', sa.String(), nullable=True),
        sa.Column('web_commit_signoff_required', sa.String(), nullable=True),
        sa.Column('members_can_create_public_pages', sa.String(), nullable=True),
        sa.Column('members_can_create_private_pages', sa.String(), nullable=True),
        sa.Column('plan_name', sa.String(), nullable=True),
        sa.Column('plan_space', sa.String(), nullable=True),
        sa.Column('plan_private_repos', sa.String(), nullable=True),
        sa.Column('plan_filled_seats', sa.String(), nullable=True),
        sa.Column('plan_seats', sa.String(), nullable=True),
        sa.Column('advanced_security_enabled_for_new_repositories', sa.String(), nullable=True),
        sa.Column('dependabot_alerts_enabled_for_new_repositories', sa.String(), nullable=True),
        sa.Column('dependabot_security_updates_enabled_for_new_repositories', sa.String(), nullable=True),
        sa.Column('dependency_graph_enabled_for_new_repositories', sa.String(), nullable=True),
        sa.Column('secret_scanning_enabled_for_new_repositories', sa.String(), nullable=True),
        sa.Column('secret_scanning_push_protection_enabled_for_new_repositories', sa.String(), nullable=True),
        sa.Column('secret_scanning_push_protection_custom_link_enabled', sa.String(), nullable=True),
        sa.Column('secret_scanning_push_protection_custom_link', sa.String(), nullable=True),
        sa.Column('secret_scanning_validity_checks_enabled', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_GITHUB',
    )
    op.create_table(
        'profcomff_invation',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('node_id', sa.String(), nullable=True),
        sa.Column('login', sa.String(), nullable=True),
        sa.Column('email', sa.String(), nullable=True),
        sa.Column('role', sa.String(), nullable=True),
        sa.Column('created_at', sa.String(), nullable=True),
        sa.Column('failed_at', sa.String(), nullable=True),
        sa.Column('failed_reason', sa.String(), nullable=True),
        sa.Column('inviter_login', sa.String(), nullable=True),
        sa.Column('inviter_id', sa.Integer(), nullable=True),
        sa.Column('inviter_node_id', sa.String(), nullable=True),
        sa.Column('inviter_avatar_url', sa.String(), nullable=True),
        sa.Column('inviter_gravatar_id', sa.String(), nullable=True),
        sa.Column('inviter_url', sa.String(), nullable=True),
        sa.Column('inviter_html_url', sa.String(), nullable=True),
        sa.Column('inviter_followers_url', sa.String(), nullable=True),
        sa.Column('inviter_following_url', sa.String(), nullable=True),
        sa.Column('inviter_gists_url', sa.String(), nullable=True),
        sa.Column('inviter_starred_url', sa.String(), nullable=True),
        sa.Column('inviter_subscriptions_url', sa.String(), nullable=True),
        sa.Column('inviter_organizations_url', sa.String(), nullable=True),
        sa.Column('inviter_repos_url', sa.String(), nullable=True),
        sa.Column('inviter_events_url', sa.String(), nullable=True),
        sa.Column('inviter_received_events_url', sa.String(), nullable=True),
        sa.Column('inviter_type', sa.String(), nullable=True),
        sa.Column('inviter_site_admin', sa.Boolean(), nullable=True),
        sa.Column('team_count', sa.Integer(), nullable=True),
        sa.Column('invitation_teams_url', sa.String(), nullable=True),
        sa.Column('invitation_source', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_GITHUB',
    )
    op.create_table(
        'profcomff_member',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('login', sa.String(), nullable=True),
        sa.Column('node_id', sa.String(), nullable=True),
        sa.Column('avatar_url', sa.String(), nullable=True),
        sa.Column('gravatar_id', sa.String(), nullable=True),
        sa.Column('url', sa.String(), nullable=True),
        sa.Column('html_url', sa.String(), nullable=True),
        sa.Column('followers_url', sa.String(), nullable=True),
        sa.Column('following_url', sa.String(), nullable=True),
        sa.Column('gists_url', sa.String(), nullable=True),
        sa.Column('starred_url', sa.String(), nullable=True),
        sa.Column('subscriptions_url', sa.String(), nullable=True),
        sa.Column('organizations_url', sa.String(), nullable=True),
        sa.Column('repos_url', sa.String(), nullable=True),
        sa.Column('events_url', sa.String(), nullable=True),
        sa.Column('received_events_url', sa.String(), nullable=True),
        sa.Column('type', sa.String(), nullable=True),
        sa.Column('site_admin', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_GITHUB',
    )
    op.create_table(
        'profcomff_repo',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('node_id', sa.String(), nullable=True),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('full_name', sa.String(), nullable=True),
        sa.Column('private', sa.Boolean(), nullable=True),
        sa.Column('owner_login', sa.String(), nullable=True),
        sa.Column('owner_id', sa.Integer(), nullable=True),
        sa.Column('owner_node_id', sa.String(), nullable=True),
        sa.Column('owner_avatar_url', sa.String(), nullable=True),
        sa.Column('owner_gravatar_id', sa.String(), nullable=True),
        sa.Column('owner_url', sa.String(), nullable=True),
        sa.Column('owner_html_url', sa.String(), nullable=True),
        sa.Column('owner_followers_url', sa.String(), nullable=True),
        sa.Column('owner_following_url', sa.String(), nullable=True),
        sa.Column('owner_gists_url', sa.String(), nullable=True),
        sa.Column('owner_starred_url', sa.String(), nullable=True),
        sa.Column('owner_subscriptions_url', sa.String(), nullable=True),
        sa.Column('owner_organizations_url', sa.String(), nullable=True),
        sa.Column('owner_repos_url', sa.String(), nullable=True),
        sa.Column('owner_events_url', sa.String(), nullable=True),
        sa.Column('owner_received_events_url', sa.String(), nullable=True),
        sa.Column('owner_type', sa.String(), nullable=True),
        sa.Column('owner_site_admin', sa.Boolean(), nullable=True),
        sa.Column('html_url', sa.String(), nullable=True),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('fork', sa.Boolean(), nullable=True),
        sa.Column('url', sa.String(), nullable=True),
        sa.Column('forks_url', sa.String(), nullable=True),
        sa.Column('keys_url', sa.String(), nullable=True),
        sa.Column('collaborators_url', sa.String(), nullable=True),
        sa.Column('teams_url', sa.String(), nullable=True),
        sa.Column('hooks_url', sa.String(), nullable=True),
        sa.Column('issue_events_url', sa.String(), nullable=True),
        sa.Column('events_url', sa.String(), nullable=True),
        sa.Column('assignees_url', sa.String(), nullable=True),
        sa.Column('branches_url', sa.String(), nullable=True),
        sa.Column('tags_url', sa.String(), nullable=True),
        sa.Column('blobs_url', sa.String(), nullable=True),
        sa.Column('git_tags_url', sa.String(), nullable=True),
        sa.Column('git_refs_url', sa.String(), nullable=True),
        sa.Column('trees_url', sa.String(), nullable=True),
        sa.Column('statuses_url', sa.String(), nullable=True),
        sa.Column('languages_url', sa.String(), nullable=True),
        sa.Column('stargazers_url', sa.String(), nullable=True),
        sa.Column('contributors_url', sa.String(), nullable=True),
        sa.Column('subscribers_url', sa.String(), nullable=True),
        sa.Column('subscription_url', sa.String(), nullable=True),
        sa.Column('commits_url', sa.String(), nullable=True),
        sa.Column('git_commits_url', sa.String(), nullable=True),
        sa.Column('comments_url', sa.String(), nullable=True),
        sa.Column('issue_comment_url', sa.String(), nullable=True),
        sa.Column('contents_url', sa.String(), nullable=True),
        sa.Column('compare_url', sa.String(), nullable=True),
        sa.Column('merges_url', sa.String(), nullable=True),
        sa.Column('archive_url', sa.String(), nullable=True),
        sa.Column('downloads_url', sa.String(), nullable=True),
        sa.Column('issues_url', sa.String(), nullable=True),
        sa.Column('pulls_url', sa.String(), nullable=True),
        sa.Column('milestones_url', sa.String(), nullable=True),
        sa.Column('notifications_url', sa.String(), nullable=True),
        sa.Column('labels_url', sa.String(), nullable=True),
        sa.Column('releases_url', sa.String(), nullable=True),
        sa.Column('deployments_url', sa.String(), nullable=True),
        sa.Column('created_at', sa.String(), nullable=True),
        sa.Column('updated_at', sa.String(), nullable=True),
        sa.Column('pushed_at', sa.String(), nullable=True),
        sa.Column('git_url', sa.String(), nullable=True),
        sa.Column('ssh_url', sa.String(), nullable=True),
        sa.Column('clone_url', sa.String(), nullable=True),
        sa.Column('svn_url', sa.String(), nullable=True),
        sa.Column('homepage', sa.String(), nullable=True),
        sa.Column('size', sa.Integer(), nullable=True),
        sa.Column('stargazers_count', sa.Integer(), nullable=True),
        sa.Column('watchers_count', sa.Integer(), nullable=True),
        sa.Column('language', sa.String(), nullable=True),
        sa.Column('has_issues', sa.Boolean(), nullable=True),
        sa.Column('has_projects', sa.Boolean(), nullable=True),
        sa.Column('has_downloads', sa.Boolean(), nullable=True),
        sa.Column('has_wiki', sa.Boolean(), nullable=True),
        sa.Column('has_pages', sa.Boolean(), nullable=True),
        sa.Column('has_discussions', sa.Boolean(), nullable=True),
        sa.Column('forks_count', sa.Integer(), nullable=True),
        sa.Column('mirror_url', sa.String(), nullable=True),
        sa.Column('archived', sa.Boolean(), nullable=True),
        sa.Column('disabled', sa.Boolean(), nullable=True),
        sa.Column('open_issues_count', sa.Integer(), nullable=True),
        sa.Column('license', sa.Integer(), nullable=True),
        sa.Column('allow_forking', sa.Boolean(), nullable=True),
        sa.Column('is_template', sa.Boolean(), nullable=True),
        sa.Column('web_commit_signoff_required', sa.Boolean(), nullable=True),
        sa.Column('topics', sa.String(), nullable=True),
        sa.Column('visibility', sa.String(), nullable=True),
        sa.Column('forks', sa.Integer(), nullable=True),
        sa.Column('open_issues', sa.Integer(), nullable=True),
        sa.Column('watchers', sa.Integer(), nullable=True),
        sa.Column('default_branch', sa.String(), nullable=True),
        sa.Column('permissions_admin', sa.Boolean(), nullable=True),
        sa.Column('permissions_maintain', sa.Boolean(), nullable=True),
        sa.Column('permissions_push', sa.Boolean(), nullable=True),
        sa.Column('permissions_triage', sa.Boolean(), nullable=True),
        sa.Column('permissions_pull', sa.Boolean(), nullable=True),
        sa.Column('license_key', sa.String(), nullable=True),
        sa.Column('license_name', sa.String(), nullable=True),
        sa.Column('license_spdx_id', sa.String(), nullable=True),
        sa.Column('license_url', sa.String(), nullable=True),
        sa.Column('license_node_id', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_GITHUB',
    )
    op.create_table(
        'profcomff_team',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('node_id', sa.String(), nullable=True),
        sa.Column('slug', sa.String(), nullable=True),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('privacy', sa.String(), nullable=True),
        sa.Column('notification_setting', sa.String(), nullable=True),
        sa.Column('url', sa.String(), nullable=True),
        sa.Column('html_url', sa.String(), nullable=True),
        sa.Column('members_url', sa.String(), nullable=True),
        sa.Column('repositories_url', sa.String(), nullable=True),
        sa.Column('permission', sa.String(), nullable=True),
        sa.Column('parent', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_GITHUB',
    )
    op.create_table(
        'profcomff_team_member',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('login', sa.String(), nullable=True),
        sa.Column('node_id', sa.String(), nullable=True),
        sa.Column('avatar_url', sa.String(), nullable=True),
        sa.Column('gravatar_id', sa.String(), nullable=True),
        sa.Column('url', sa.String(), nullable=True),
        sa.Column('html_url', sa.String(), nullable=True),
        sa.Column('followers_url', sa.String(), nullable=True),
        sa.Column('following_url', sa.String(), nullable=True),
        sa.Column('gists_url', sa.String(), nullable=True),
        sa.Column('starred_url', sa.String(), nullable=True),
        sa.Column('subscriptions_url', sa.String(), nullable=True),
        sa.Column('organizations_url', sa.String(), nullable=True),
        sa.Column('repos_url', sa.String(), nullable=True),
        sa.Column('events_url', sa.String(), nullable=True),
        sa.Column('received_events_url', sa.String(), nullable=True),
        sa.Column('type', sa.String(), nullable=True),
        sa.Column('site_admin', sa.Boolean(), nullable=True),
        sa.Column('team_id', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id', 'team_id'),
        schema='STG_GITHUB',
    )
    op.create_table(
        'profcomff_team_repo',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('team_id', sa.Integer(), nullable=True),
        sa.Column('node_id', sa.String(), nullable=True),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('full_name', sa.String(), nullable=True),
        sa.Column('private', sa.String(), nullable=True),
        sa.Column('owner_login', sa.String(), nullable=True),
        sa.Column('owner_id', sa.Integer(), nullable=True),
        sa.Column('owner_node_id', sa.String(), nullable=True),
        sa.Column('owner_avatar_url', sa.String(), nullable=True),
        sa.Column('owner_gravatar_id', sa.String(), nullable=True),
        sa.Column('owner_url', sa.String(), nullable=True),
        sa.Column('owner_html_url', sa.String(), nullable=True),
        sa.Column('owner_followers_url', sa.String(), nullable=True),
        sa.Column('owner_following_url', sa.String(), nullable=True),
        sa.Column('owner_gists_url', sa.String(), nullable=True),
        sa.Column('owner_starred_url', sa.String(), nullable=True),
        sa.Column('owner_subscriptions_url', sa.String(), nullable=True),
        sa.Column('owner_organizations_url', sa.String(), nullable=True),
        sa.Column('owner_repos_url', sa.String(), nullable=True),
        sa.Column('owner_events_url', sa.String(), nullable=True),
        sa.Column('owner_received_events_url', sa.String(), nullable=True),
        sa.Column('owner_type', sa.String(), nullable=True),
        sa.Column('owner_site_admin', sa.String(), nullable=True),
        sa.Column('html_url', sa.String(), nullable=True),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('fork', sa.String(), nullable=True),
        sa.Column('url', sa.String(), nullable=True),
        sa.Column('forks_url', sa.String(), nullable=True),
        sa.Column('keys_url', sa.String(), nullable=True),
        sa.Column('collaborators_url', sa.String(), nullable=True),
        sa.Column('teams_url', sa.String(), nullable=True),
        sa.Column('hooks_url', sa.String(), nullable=True),
        sa.Column('issue_events_url', sa.String(), nullable=True),
        sa.Column('events_url', sa.String(), nullable=True),
        sa.Column('assignees_url', sa.String(), nullable=True),
        sa.Column('branches_url', sa.String(), nullable=True),
        sa.Column('tags_url', sa.String(), nullable=True),
        sa.Column('blobs_url', sa.String(), nullable=True),
        sa.Column('git_tags_url', sa.String(), nullable=True),
        sa.Column('git_refs_url', sa.String(), nullable=True),
        sa.Column('trees_url', sa.String(), nullable=True),
        sa.Column('statuses_url', sa.String(), nullable=True),
        sa.Column('languages_url', sa.String(), nullable=True),
        sa.Column('stargazers_url', sa.String(), nullable=True),
        sa.Column('contributors_url', sa.String(), nullable=True),
        sa.Column('subscribers_url', sa.String(), nullable=True),
        sa.Column('subscription_url', sa.String(), nullable=True),
        sa.Column('commits_url', sa.String(), nullable=True),
        sa.Column('git_commits_url', sa.String(), nullable=True),
        sa.Column('comments_url', sa.String(), nullable=True),
        sa.Column('issue_comment_url', sa.String(), nullable=True),
        sa.Column('contents_url', sa.String(), nullable=True),
        sa.Column('compare_url', sa.String(), nullable=True),
        sa.Column('merges_url', sa.String(), nullable=True),
        sa.Column('archive_url', sa.String(), nullable=True),
        sa.Column('downloads_url', sa.String(), nullable=True),
        sa.Column('issues_url', sa.String(), nullable=True),
        sa.Column('pulls_url', sa.String(), nullable=True),
        sa.Column('milestones_url', sa.String(), nullable=True),
        sa.Column('notifications_url', sa.String(), nullable=True),
        sa.Column('labels_url', sa.String(), nullable=True),
        sa.Column('releases_url', sa.String(), nullable=True),
        sa.Column('deployments_url', sa.String(), nullable=True),
        sa.Column('created_at', sa.String(), nullable=True),
        sa.Column('updated_at', sa.String(), nullable=True),
        sa.Column('pushed_at', sa.String(), nullable=True),
        sa.Column('git_url', sa.String(), nullable=True),
        sa.Column('ssh_url', sa.String(), nullable=True),
        sa.Column('clone_url', sa.String(), nullable=True),
        sa.Column('svn_url', sa.String(), nullable=True),
        sa.Column('homepage', sa.String(), nullable=True),
        sa.Column('size', sa.Integer(), nullable=True),
        sa.Column('stargazers_count', sa.Integer(), nullable=True),
        sa.Column('watchers_count', sa.Integer(), nullable=True),
        sa.Column('language', sa.String(), nullable=True),
        sa.Column('has_issues', sa.String(), nullable=True),
        sa.Column('has_projects', sa.String(), nullable=True),
        sa.Column('has_downloads', sa.String(), nullable=True),
        sa.Column('has_wiki', sa.String(), nullable=True),
        sa.Column('has_pages', sa.String(), nullable=True),
        sa.Column('forks_count', sa.Integer(), nullable=True),
        sa.Column('mirror_url', sa.String(), nullable=True),
        sa.Column('archived', sa.String(), nullable=True),
        sa.Column('disabled', sa.String(), nullable=True),
        sa.Column('open_issues_count', sa.Integer(), nullable=True),
        sa.Column('license_key', sa.String(), nullable=True),
        sa.Column('license_name', sa.String(), nullable=True),
        sa.Column('license_spdx_id', sa.String(), nullable=True),
        sa.Column('license_url', sa.String(), nullable=True),
        sa.Column('license_node_id', sa.String(), nullable=True),
        sa.Column('allow_forking', sa.String(), nullable=True),
        sa.Column('topics', sa.String(), nullable=True),
        sa.Column('visibility', sa.String(), nullable=True),
        sa.Column('forks', sa.Integer(), nullable=True),
        sa.Column('open_issues', sa.Integer(), nullable=True),
        sa.Column('watchers', sa.Integer(), nullable=True),
        sa.Column('default_branch', sa.String(), nullable=True),
        sa.Column('permissions_admin', sa.String(), nullable=True),
        sa.Column('permissions_maintain', sa.String(), nullable=True),
        sa.Column('permissions_push', sa.String(), nullable=True),
        sa.Column('permissions_triage', sa.String(), nullable=True),
        sa.Column('permissions_pull', sa.String(), nullable=True),
        sa.Column('role_name', sa.String(), nullable=True),
        sa.Column('license', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id', 'team_id'),
        schema='STG_GITHUB',
    )
    op.create_group(
        "test_dwh_stg_github_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_read"
    )
    op.create_group(
        "test_dwh_stg_github_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_write"
    )
    op.create_group(
        "test_dwh_stg_github_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_all"
    )
    op.grant_on_schema(
        "test_dwh_stg_github_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_read",
        "STG_GITHUB",
    )
    op.grant_on_schema(
        "test_dwh_stg_github_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_write",
        "STG_GITHUB",
    )
    op.grant_on_schema(
        "test_dwh_stg_github_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_all",
        "STG_GITHUB",
    )
    op.grant_on_table(
        "test_dwh_stg_github_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_read",
        ['SELECT'],
        '"STG_GITHUB".org_info',
    )
    op.grant_on_table(
        "test_dwh_stg_github_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_read",
        ['SELECT'],
        '"STG_GITHUB".profcomff_invation',
    )
    op.grant_on_table(
        "test_dwh_stg_github_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_read",
        ['SELECT'],
        '"STG_GITHUB".profcomff_member',
    )
    op.grant_on_table(
        "test_dwh_stg_github_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_read",
        ['SELECT'],
        '"STG_GITHUB".profcomff_repo',
    )
    op.grant_on_table(
        "test_dwh_stg_github_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_read",
        ['SELECT'],
        '"STG_GITHUB".profcomff_team',
    )
    op.grant_on_table(
        "test_dwh_stg_github_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_read",
        ['SELECT'],
        '"STG_GITHUB".profcomff_team_member',
    )
    op.grant_on_table(
        "test_dwh_stg_github_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_read",
        ['SELECT'],
        '"STG_GITHUB".profcomff_team_repo',
    )
    op.grant_on_table(
        "test_dwh_stg_github_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_GITHUB".org_info',
    )
    op.grant_on_table(
        "test_dwh_stg_github_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_GITHUB".profcomff_invation',
    )
    op.grant_on_table(
        "test_dwh_stg_github_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_GITHUB".profcomff_member',
    )
    op.grant_on_table(
        "test_dwh_stg_github_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_GITHUB".profcomff_repo',
    )
    op.grant_on_table(
        "test_dwh_stg_github_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_GITHUB".profcomff_team',
    )
    op.grant_on_table(
        "test_dwh_stg_github_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_GITHUB".profcomff_team_member',
    )
    op.grant_on_table(
        "test_dwh_stg_github_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_GITHUB".profcomff_team_repo',
    )
    op.grant_on_table(
        "test_dwh_stg_github_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_all",
        ['ALL'],
        '"STG_GITHUB".org_info',
    )
    op.grant_on_table(
        "test_dwh_stg_github_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_all",
        ['ALL'],
        '"STG_GITHUB".profcomff_invation',
    )
    op.grant_on_table(
        "test_dwh_stg_github_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_all",
        ['ALL'],
        '"STG_GITHUB".profcomff_member',
    )
    op.grant_on_table(
        "test_dwh_stg_github_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_all",
        ['ALL'],
        '"STG_GITHUB".profcomff_repo',
    )
    op.grant_on_table(
        "test_dwh_stg_github_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_all",
        ['ALL'],
        '"STG_GITHUB".profcomff_team',
    )
    op.grant_on_table(
        "test_dwh_stg_github_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_all",
        ['ALL'],
        '"STG_GITHUB".profcomff_team_member',
    )
    op.grant_on_table(
        "test_dwh_stg_github_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_all",
        ['ALL'],
        '"STG_GITHUB".profcomff_team_repo',
    )


def downgrade():
    op.revoke_on_schema(
        "test_dwh_stg_github_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_all",
        "STG_GITHUB",
    )
    op.revoke_on_schema(
        ("test_dwh_stg_github_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_write"),
        "STG_GITHUB",
    )
    op.revoke_on_schema(
        ("test_dwh_stg_github_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_read"),
        "STG_GITHUB",
    )
    op.drop_table('profcomff_team_repo', schema='STG_GITHUB')
    op.drop_table('profcomff_team_member', schema='STG_GITHUB')
    op.drop_table('profcomff_team', schema='STG_GITHUB')
    op.drop_table('profcomff_repo', schema='STG_GITHUB')
    op.drop_table('profcomff_member', schema='STG_GITHUB')
    op.drop_table('profcomff_invation', schema='STG_GITHUB')
    op.drop_table('org_info', schema='STG_GITHUB')
    op.delete_group(
        "test_dwh_stg_github_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_all"
    )
    op.delete_group(
        "test_dwh_stg_github_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_write"
    )
    op.delete_group(
        "test_dwh_stg_github_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_github_read"
    )
    op.drop_table_schema("STG_GITHUB")
