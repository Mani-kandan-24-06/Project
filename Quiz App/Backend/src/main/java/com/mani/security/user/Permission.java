package com.mani.security.user;

import lombok.Getter;
import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
public enum Permission {

    ADMIN_READ("admin:read"),
    ADMIN_UPDATE("admin:update"),
    ADMIN_CREATE("admin:create"),
    ADMIN_DELETE("admin:delete"),
    CANDIDATE_READ("candidate:read"),
    CANDIDATE_UPDATE("candidate:update"),
    CANDIDATE_CREATE("candidate:create"),
    CANDIDATE_DELETE("candidate:delete")

    ;

    @Getter
    private final String permission;
}
