package com.example.api;

import com.example.api.entities.Topic;
import com.example.api.entities.Users;
import com.example.api.entities.Videos;
import jakarta.persistence.*;
import lombok.*;

@Entity
@AllArgsConstructor
@NoArgsConstructor
@Getter
@Setter
@Builder
public class Favorites {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long favoriteId;

    @OneToOne(mappedBy = "favorite")
    private Users user;
}
